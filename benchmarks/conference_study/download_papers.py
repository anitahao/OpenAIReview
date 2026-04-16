#!/usr/bin/env python
"""Download ICLR papers for the accepted-vs-rejected study.

Fetches the papercopilot ICLR dataset, selects N accepted (Outstanding/Oral)
and N rejected papers, downloads their PDFs from OpenReview, and writes an
updated manifest.json.

Usage:
    python download_papers.py                    # 5 per group (default)
    python download_papers.py -n 10              # 10 per group
    python download_papers.py -n 8 --year 2025   # 8 per group from ICLR 2025
    python download_papers.py --min-pages 15     # reject papers shorter than 15 pages

Selection criteria:
    Accepted: status in {Oral, Spotlight} (Outstanding Papers).
    Rejected: status = Reject, rating_avg in [2.5, 3.5], >= 3 reviewers,
              avg review word-count > 400 (substantive reviews).
    Both groups filtered to >= --min-pages pages (default 15).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

PAPERCOPILOT_URL = (
    "https://raw.githubusercontent.com/Papercopilot/paperlists/main"
    "/iclr/iclr{year}.json"
)


def fetch_dataset(year: int, cache_dir: Path) -> list[dict]:
    """Download (or load cached) papercopilot ICLR dataset."""
    cache = cache_dir / f"iclr{year}.json"
    if cache.exists():
        print(f"Using cached dataset: {cache}")
        return json.loads(cache.read_text())

    url = PAPERCOPILOT_URL.format(year=year)
    print(f"Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(data)
    return json.loads(data)


def avg_field(paper: dict, key: str) -> float | None:
    """Extract average from papercopilot's [mean, std] lists."""
    v = paper.get(key)
    if isinstance(v, list) and v:
        return v[0]
    return None


def select_accepted(dataset: list[dict], n: int) -> list[dict]:
    """Pick N accepted papers (Oral/Spotlight, highest-rated first)."""
    candidates = []
    for p in dataset:
        if p["status"] not in ("Oral", "Spotlight"):
            continue
        r = avg_field(p, "rating_avg")
        if r is None:
            continue
        candidates.append((r, p))
    candidates.sort(key=lambda x: -x[0])  # highest rating first
    if len(candidates) < n:
        print(f"  Warning: only {len(candidates)} Oral/Spotlight papers available, "
              f"requested {n}")
    return [p for _, p in candidates[:n]]


def select_rejected(dataset: list[dict], n: int,
                    rating_range: tuple[float, float] = (2.5, 3.5)) -> list[dict]:
    """Pick N rejected papers with substantive reviews.

    Filters: status=Reject, rating_avg in range, >= 3 reviewers,
    avg review word-count > 400.
    """
    lo, hi = rating_range
    candidates = []
    for p in dataset:
        if p["status"] != "Reject":
            continue
        r = avg_field(p, "rating_avg")
        wc = avg_field(p, "wc_review_avg")
        n_rev = len(p.get("rating", "").split(";")) if p.get("rating") else 0
        if r is None or wc is None:
            continue
        if not (lo <= r <= hi) or wc < 400 or n_rev < 3:
            continue
        pdf_kb = (p.get("pdf_size") or 0) / 1024
        candidates.append((pdf_kb, r, p))
    # Sort by PDF size descending (proxy for longer papers)
    candidates.sort(key=lambda x: -x[0])
    if len(candidates) < n:
        print(f"  Warning: only {len(candidates)} eligible rejected papers, "
              f"requested {n}")
    return [p for _, _, p in candidates[:n]]


def download_pdf(forum_id: str, dest: Path) -> bool:
    """Download a PDF from OpenReview. Returns True on success."""
    if dest.exists() and dest.stat().st_size > 10_000:
        return True
    url = f"https://openreview.net/pdf?id={forum_id}"
    result = subprocess.run(
        ["curl", "-sL", "-A", UA, "-o", str(dest), "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    code = result.stdout.strip()
    size = dest.stat().st_size if dest.exists() else 0
    return code == "200" and size > 10_000


def get_page_count(pdf_path: Path) -> int:
    """Return page count of a PDF using pymupdf."""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        n = len(doc)
        doc.close()
        return n
    except Exception:
        return 0


def slugify(title: str, prefix: str) -> str:
    """Create a slug from a paper title."""
    import re
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")[:60]
    return f"{prefix}-{s}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", "--num", type=int, default=5,
                    help="Number of papers per group (default: 5)")
    ap.add_argument("--year", type=int, default=2024,
                    help="ICLR year (default: 2024)")
    ap.add_argument("--min-pages", type=int, default=15,
                    help="Minimum page count to keep a paper (default: 15)")
    ap.add_argument("--output-dir", type=str, default=str(HERE),
                    help="Output directory (default: script directory)")
    ap.add_argument("--rating-lo", type=float, default=2.5,
                    help="Minimum rating_avg for rejected papers (default: 2.5)")
    ap.add_argument("--rating-hi", type=float, default=3.5,
                    help="Maximum rating_avg for rejected papers (default: 3.5)")
    args = ap.parse_args()

    out_dir = Path(args.output_dir)
    acc_dir = out_dir / "papers" / "accepted"
    rej_dir = out_dir / "papers" / "rejected"
    acc_dir.mkdir(parents=True, exist_ok=True)
    rej_dir.mkdir(parents=True, exist_ok=True)
    cache_dir = out_dir / ".cache"

    year = args.year
    n = args.num
    min_pages = args.min_pages

    # Step 1: Fetch dataset
    dataset = fetch_dataset(year, cache_dir)
    print(f"Dataset: {len(dataset)} ICLR {year} submissions")

    # Step 2: Select candidates (fetch extra to account for page-count filtering)
    extra = max(n * 2, n + 10)
    acc_candidates = select_accepted(dataset, extra)
    rej_candidates = select_rejected(dataset, extra,
                                     rating_range=(args.rating_lo, args.rating_hi))
    print(f"Accepted candidates: {len(acc_candidates)}")
    print(f"Rejected candidates: {len(rej_candidates)}")

    # Step 3: Download and filter by page count
    manifest_papers = []
    for group, candidates, dest_dir, prefix in [
        ("accepted", acc_candidates, acc_dir, f"iclr{year % 100}-acc"),
        ("rejected", rej_candidates, rej_dir, f"iclr{year % 100}-rej"),
    ]:
        print(f"\nDownloading {group} papers (target: {n})...")
        picked = 0
        for p in candidates:
            if picked >= n:
                break
            slug = slugify(p["title"], prefix)
            pdf_path = dest_dir / f"{slug}.pdf"

            ok = download_pdf(p["id"], pdf_path)
            if not ok:
                print(f"  FAIL  {slug}  (download error)")
                continue

            pages = get_page_count(pdf_path)
            if pages < min_pages:
                print(f"  SKIP  {slug}  ({pages} pages < {min_pages} min)")
                pdf_path.unlink(missing_ok=True)
                continue

            picked += 1
            print(f"  [{picked}/{n}] {slug}  ({pages} pages, "
                  f"{pdf_path.stat().st_size // 1024}kb)")

            entry = {
                "slug": slug,
                "group": group,
                "forum_id": p["id"],
                "title": p["title"],
                "pages": pages,
                "rating": p.get("rating", ""),
                "rating_avg": avg_field(p, "rating_avg"),
                "soundness": p.get("soundness", ""),
                "soundness_avg": avg_field(p, "soundness_avg"),
                "confidence": p.get("confidence", ""),
                "confidence_avg": avg_field(p, "confidence_avg"),
                "contribution": p.get("contribution", ""),
                "contribution_avg": avg_field(p, "contribution_avg"),
                "presentation": p.get("presentation", ""),
                "presentation_avg": avg_field(p, "presentation_avg"),
            }
            if group == "accepted":
                entry["award"] = p["status"]  # Oral or Spotlight
            manifest_papers.append(entry)

            time.sleep(0.5)

        if picked < n:
            print(f"  Warning: only got {picked}/{n} {group} papers")

    # Step 4: Write manifest
    manifest = {
        "description": (f"ICLR {year} papers for OpenAIReview accepted-vs-rejected "
                        f"comparison study. {n} per group."),
        "venue": f"ICLR {year}",
        "papers": manifest_papers,
        "models": [
            "google/gemini-3-flash-preview",
            "z-ai/glm-4.6",
            "qwen/qwen3-235b-a22b-2507",
        ],
        "review_caps": {
            "max_pages": 20,
            "max_tokens": 20_000,
        },
    }

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"\nManifest written: {manifest_path}")
    print(f"  {sum(1 for p in manifest_papers if p['group'] == 'accepted')} accepted, "
          f"{sum(1 for p in manifest_papers if p['group'] == 'rejected')} rejected")
    print(f"  Reviewer scores included (rating, soundness, contribution, presentation)")


if __name__ == "__main__":
    main()
