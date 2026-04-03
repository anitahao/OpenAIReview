#!/usr/bin/env python3
"""Run perturb → review → score on proof-pile arxiv papers.

Results layout:
  results/
    perturb/
      paper_001/
      paper_002/
      ...
    <review-model>/
      <method>/
        paper_001/
          review/
          score/
        paper_002/
          ...
"""

import re
import json
import os
import subprocess
import tempfile
from pathlib import Path

from datasets import load_dataset

# ---------------------------------------------------------------------------
# Config — edit these as needed
# ---------------------------------------------------------------------------

MAX_PAPERS = 2

GENERATE_METHOD = "llm"  # "rules" or "llm"

PERTURB_MODEL = "google/gemini-3.1-pro-preview"  # only used when GENERATE_METHOD = "llm"

REVIEW_MODELS = [
    "google/gemini-3.1-pro-preview",
    # "anthropic/claude-opus-4-6",
    # "anthropic/claude-sonnet-4-6",
    # "openai/gpt-4o",
    # "google/gemini-2.5-pro",
]

SCORE_MODEL = "google/gemini-3.1-pro-preview" 

REVIEW_METHODS = [
    "zero_shot",
    "local",
    "progressive",
]

RESULTS_DIR = Path("results")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def paper_length(paper: dict) -> int:
    text = re.sub(r'\\[a-zA-Z]+\*?', ' ', paper['text'])
    text = re.sub(r'[\{\}\$\[\]]', ' ', text)
    return len(text.split())


def model_slug(model: str) -> str:
    """e.g. 'anthropic/claude-opus-4-6' -> 'claude-opus-4-6'"""
    return model.split("/")[-1]


def run(cmd: list[str]) -> int:
    print(f"    $ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd).returncode


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading proof-pile dataset (streaming)...")
    ds = load_dataset("hoskinson-center/proof-pile", split="train", streaming=True)

    papers_short = [] # 2k-7k
    papers_medium = [] # 7k-17k
    papers_long = [] # > 17k

    papers_all = []
    for paper in ds:
        meta = json.loads(paper["meta"]) if isinstance(paper["meta"], str) else paper["meta"]
        if meta.get("config", "") == "arxiv":
            papers_all.append(paper)

            # group by length 
            if paper_length(paper) > 2000 and paper_length(paper) <= 7000:
                papers_short.append(paper)
            elif paper_length(paper) > 7000 and paper_length(paper) <= 17000: 
                papers_medium.append(paper)
            else:
                papers_long.append(paper)

            if len(papers_all) >= MAX_PAPERS:
                break

    print(f"Collected {len(papers_short)} arxiv papers\n")

    RESULTS_DIR.mkdir(exist_ok=True)

    papers = papers_short # CHANGE ACCORDING TO PREFERENCES

    for i, paper in enumerate(papers, start=1):
        paper_label = f"paper_{i:03d}"
        perturb_dir = RESULTS_DIR / "perturb" / paper_label
        perturb_dir.mkdir(parents=True, exist_ok=True)

        print(f"{'='*60}")
        print(f"Paper {i:03d}/{MAX_PAPERS}  ({paper_length(paper):,} words)")
        print(f"{'='*60}")

        # Write paper text to a temp file
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", prefix=f"paper_{i:03d}_", delete=False
        )
        tmp.write(paper["text"])
        tmp.close()
        tmp_path = Path(tmp.name)

        try:
            # ------------------------------------------------------------------
            # Step 1: Perturb (once per paper)
            # ------------------------------------------------------------------
            print(f"\n  [1] Perturb  (model: {model_slug(PERTURB_MODEL)})")
            rc = run(["openaireview", "perturb", str(tmp_path),
                      "--output-dir", str(perturb_dir),
                      "--generate", GENERATE_METHOD,
                      "--model", PERTURB_MODEL])
            if rc != 0:
                print(f"  perturb failed (exit {rc}), skipping paper")
                continue

            manifest = next(perturb_dir.glob("*_perturbations.json"), None)
            corrupted = next(perturb_dir.glob("*_corrupted.md"), None)
            if not manifest or not corrupted:
                print("  perturb outputs missing, skipping paper")
                continue

            # ------------------------------------------------------------------
            # Steps 2+3: Review + Score for every (model, method) combination
            # ------------------------------------------------------------------
            for model in REVIEW_MODELS:
                for method in REVIEW_METHODS:
                    paper_dir = RESULTS_DIR / model_slug(model) / method / paper_label
                    review_dir = paper_dir / "review"
                    score_dir = paper_dir / "score"
                    review_dir.mkdir(parents=True, exist_ok=True)
                    score_dir.mkdir(parents=True, exist_ok=True)

                    print(f"\n  [2] Review  ({model_slug(model)} / {method})")
                    rc = run(["openaireview", "review", str(corrupted),
                              "--method", method,
                              "--output-dir", str(review_dir),
                              "--model", model])
                    if rc != 0:
                        print(f"  review failed (exit {rc}), skipping")
                        continue

                    review_json = next(review_dir.glob("*.json"), None)
                    if not review_json:
                        print("  review output missing, skipping")
                        continue

                    print(f"\n  [3] Score   ({model_slug(model)} / {method})")
                    rc = run(["openaireview", "score", str(manifest), str(review_json),
                              "--model", SCORE_MODEL,
                              "--output-dir", str(score_dir)])
                    if rc != 0:
                        print(f"  score failed (exit {rc}), skipping")
                        continue

            print(f"\n  Done: {paper_label}")

        finally:
            tmp_path.unlink(missing_ok=True)

    print(f"\nAll done. Results in {RESULTS_DIR}/")


if __name__ == "__main__":
    main()
