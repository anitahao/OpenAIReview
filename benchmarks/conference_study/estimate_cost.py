#!/usr/bin/env python
"""Dry-run cost estimator for the conference accept-vs-reject study.

For each downloaded PDF and each model in the manifest, estimate the total
USD cost of running `openaireview review --method progressive` with the
same caps the batch runner will use. Reads caps from the same YAML config
that run_study.py consumes, so the estimate matches the planned run.

The progressive method, as observed in past benchmark runs, sends ~6x the
input token count through the LLM (running summary + window context replay
across passages + final consolidation + overall feedback). Completion is
~0.15x input. We use those multipliers to estimate.

Run:
    python estimate_cost.py --config configs/baseline.yaml
    python estimate_cost.py --max-pages 30              # ad-hoc
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

# Resolve repo paths and import the same parser/tokenizer the CLI uses.
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "src"))

from reviewer.parsers import parse_document  # noqa: E402
from reviewer.utils import count_tokens  # noqa: E402

# Defaults — overridden by YAML config and/or CLI flags in main().
DEFAULT_MAX_PAGES = 20
DEFAULT_MAX_TOKENS = 20_000

# Runtime values, populated in main().
MAX_PAGES: int = DEFAULT_MAX_PAGES
MAX_TOKENS: int = DEFAULT_MAX_TOKENS

# Empirically observed scale factors for progressive mode.
# (Total prompt tokens sent to LLM) / (input doc tokens) ≈ 6
# (Total completion tokens) / (input doc tokens) ≈ 0.15
PROMPT_MULT = 6.0
COMPLETION_MULT = 0.15

# OpenRouter prices (USD per token). Verified live from openrouter.ai/api/v1/models.
MODEL_PRICES = {
    "google/gemini-3-flash-preview": {"prompt": 0.50e-6, "completion": 3.00e-6},
    "z-ai/glm-4.6":                  {"prompt": 0.39e-6, "completion": 1.90e-6},
    "qwen/qwen3-235b-a22b-2507":     {"prompt": 0.071e-6,"completion": 0.10e-6},
}


def estimate_paper(pdf_path: Path) -> int:
    """Return the *effective* input token count for one PDF."""
    title, content, _was_ocr = parse_document(pdf_path, max_pages=MAX_PAGES)
    n = count_tokens(content)
    return min(n, MAX_TOKENS)


def load_config(path: str) -> dict:
    """Load a YAML run-config file. Returns {} if path is None."""
    if not path:
        return {}
    cfg_path = Path(path)
    if not cfg_path.is_absolute():
        cfg_path = cfg_path if cfg_path.exists() else HERE / path
    if not cfg_path.exists():
        sys.exit(f"config file not found: {path}")
    with cfg_path.open() as f:
        return yaml.safe_load(f) or {}


def main() -> None:
    global MAX_PAGES, MAX_TOKENS

    ap = argparse.ArgumentParser()
    ap.add_argument("--config", help="YAML config file (same schema as run_study.py).")
    ap.add_argument("--max-pages", type=int, default=None,
                    help=f"Override max pages (default: {DEFAULT_MAX_PAGES}).")
    ap.add_argument("--max-tokens", type=int, default=None,
                    help=f"Override max tokens (default: {DEFAULT_MAX_TOKENS}).")
    args = ap.parse_args()

    cfg = load_config(args.config)
    MAX_PAGES = args.max_pages if args.max_pages is not None \
        else cfg.get("max_pages", DEFAULT_MAX_PAGES)
    MAX_TOKENS = args.max_tokens if args.max_tokens is not None \
        else cfg.get("max_tokens", DEFAULT_MAX_TOKENS)

    manifest = json.loads((HERE / "manifest.json").read_text())
    papers = manifest["papers"]
    models = manifest["models"]

    if args.config:
        print(f"Config: {args.config}")
        if cfg.get("name"):
            print(f"Experiment: {cfg['name']}")
    # Per-paper effective tokens (parse once).
    print(f"Parsing {len(papers)} PDFs (max {MAX_PAGES} pages, truncated to "
          f"{MAX_TOKENS:,} tokens)...\n")
    paper_tokens: dict[str, int] = {}
    for p in papers:
        pdf = HERE / "papers" / p["group"] / f"{p['slug']}.pdf"
        n = estimate_paper(pdf)
        paper_tokens[p["slug"]] = n
        print(f"  {p['slug']:42s} {n:>6,} tokens  ({p['group']})")

    # Cost table.
    print("\n\nEstimated cost per (paper x model), USD:")
    header = f"{'paper':42s}  " + "  ".join(
        f"{m.split('/')[-1]:>26s}" for m in models
    ) + "       row total"
    print(header)
    print("-" * len(header))

    grand_total = 0.0
    by_group = {"accepted": 0.0, "rejected": 0.0}
    by_model = {m: 0.0 for m in models}

    for p in papers:
        n = paper_tokens[p["slug"]]
        prompt_tok = n * PROMPT_MULT
        comp_tok = n * COMPLETION_MULT
        row = []
        row_total = 0.0
        for m in models:
            price = MODEL_PRICES[m]
            cost = prompt_tok * price["prompt"] + comp_tok * price["completion"]
            row.append(f"${cost:6.4f}")
            row_total += cost
            by_model[m] += cost
        grand_total += row_total
        by_group[p["group"]] += row_total
        print(f"  {p['slug']:42s} " +
              "  ".join(f"{c:>26s}" for c in row) +
              f"  ${row_total:6.3f}")

    print("-" * len(header))
    print(f"  {'totals by model':42s} " +
          "  ".join(f"{'$' + format(by_model[m], '6.3f'):>26s}" for m in models) +
          f"  ${grand_total:6.3f}")

    print()
    print(f"Group totals:  accepted=${by_group['accepted']:.3f}  "
          f"rejected=${by_group['rejected']:.3f}")
    print(f"GRAND TOTAL ESTIMATE: ${grand_total:.2f}")
    print()
    print("Notes:")
    print(f"  - Assumes prompt-token multiplier {PROMPT_MULT}x and completion "
          f"multiplier {COMPLETION_MULT}x of input doc tokens.")
    print("  - Real cost can vary +/- 30% depending on consolidation length and")
    print("    how many passages the paper splits into.")


if __name__ == "__main__":
    main()
