#!/usr/bin/env python
"""Dry-run cost estimator for the conference accept-vs-reject study.

For each downloaded PDF and each of the 3 OpenRouter models, estimate the
total USD cost of running `openaireview review --method progressive` with
the same caps the batch runner will use (--max-pages 20 --max-tokens 20000).

The progressive method, as observed in past benchmark runs, sends ~6x the
input token count through the LLM (running summary + window context replay
across passages + final consolidation + overall feedback). Completion is
~0.15x input. We use those multipliers to estimate.

Run:
    python estimate_cost.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Resolve repo paths and import the same parser/tokenizer the CLI uses.
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "src"))

from reviewer.parsers import parse_document  # noqa: E402
from reviewer.utils import count_tokens  # noqa: E402

# Match runner caps.
MAX_PAGES = 20
MAX_TOKENS = 20_000

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


def main() -> None:
    manifest = json.loads((HERE / "manifest.json").read_text())
    papers = manifest["papers"]
    models = manifest["models"]

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
