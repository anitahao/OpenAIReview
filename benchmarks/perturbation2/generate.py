"""LLM-based error generation from candidate spans.

Stage 1: LLM picks from pre-extracted candidates and creates perturbations.
Stage 2: LLM proposes free-form errors the extraction missed (validated by fuzzy match).
"""

import json
import re

from reviewer.client import chat
from .models import (
    CandidateSpan,
    ErrorCategory,
    Perturbation,
)

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

"""
You are generating seeded perturbations for an academic paper review benchmark.

Below are candidate spans extracted from the paper. Each has a span_id, type, \
the exact text, and surrounding context.

IMPORTANT RULES:
- Choose spans where a minimal edit creates an internally inconsistent paper
- The error must be verifiable from the paper text alone, not external knowledge
- Do NOT perturb spans that look OCR-corrupted or ambiguous
- Each perturbation must target a DIFFERENT fact or equation
- Aim for {n_per_category} perturbations per category when possible

CANDIDATES:
{candidates_json}

For each perturbation, return:
- span_id: which candidate to perturb
- category: one of {categories}
- perturbed: the replacement text (must differ from original)
- why_wrong: how a reader can verify this is wrong using only the paper

Return ONLY a JSON array of perturbation objects. No commentary."""

# V2
STAGE1_PROMPT = r"""
You are creating seeded errors in academic math papers to benchmark LLM reviewers.

Given candidate spans from a paper, select spans and introduce a single minimal error
per span. Errors should be subtle enough that a careful reviewer could catch them,
but not so obvious they are immediately apparent.

ERROR CATEGORIES (only use these):
- operator_or_sign: flip an operator or sign (+ becomes -, \leq becomes \geq, \cup becomes \cap)
- symbol_binding: replace a symbol with a similar but wrong one (e.g. \alpha becomes \beta, \mu becomes \sigma)
- index_or_subscript: change a subscript or superscript (e.g. x_i becomes x_{{i+1}}, A^n becomes A^{{n-1}})
- numeric_parameter: change a numeric value (e.g. 0.5 becomes 0.25, n=100 becomes n=200)

RULES:
- Make exactly ONE change per perturbation (minimal edit)
- The perturbed text must be valid LaTeX
- The error must be detectable from the paper text alone (no external knowledge needed)
- Do NOT select spans that look malformed or OCR-corrupted
- Each perturbation must target a different span
- Aim for {n_per_category} perturbations per category

CANDIDATES:
{candidates_json}

For each perturbation, return:
- span_id: which candidate to perturb
- category: one of {categories}
- perturbed: the replacement text (must differ from original)
- why_wrong: how a reader can verify this is wrong using only the paper

Return ONLY a JSON array of perturbation objects. No commentary.
"""

# ---------------------------------------------------------------------------
# Stage 1:
# ---------------------------------------------------------------------------

def generate_stage1(
    candidates: list[CandidateSpan],
    model: str = "anthropic/claude-opus-4-6",
    n_per_category: int = 2,
    reasoning_effort: str | None = None,
) -> list[Perturbation]:
    """Ask the LLM to create perturbations from pre-extracted candidates."""
    cat_group = [
        ErrorCategory.OPERATOR_OR_SIGN,
        ErrorCategory.SYMBOL_BINDING,
        ErrorCategory.INDEX_OR_SUBSCRIPT,
        ErrorCategory.NUMERIC_PARAMETER,
    ]

    all_perturbations: list[Perturbation] = []

    # Build candidate JSON for the prompt
    candidates_json = json.dumps([
        {
            "span_id": c.span_id,
            "type": c.span_type.value,
            "text": c.text,
            "context": c.context,
            "compatible_categories": [cat.value for cat in c.compatible_categories],
        }
        for c in candidates
    ], indent=2)

    prompt = STAGE1_PROMPT.format(
        n_per_category=n_per_category,
        candidates_json=candidates_json,
        categories=", ".join(c.value for c in cat_group),
    )

    print(f"  Stage 1: {len(candidates)} candidates...")

    response, usage = chat(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        max_tokens=8192,
        reasoning_effort=reasoning_effort,
    )

    perturbations = _parse_stage1_response(response, candidates)
    all_perturbations.extend(perturbations)
    print(f"    -> {len(perturbations)} perturbations")

    return all_perturbations


def _parse_stage1_response(
    response: str,
    candidates: list[CandidateSpan],
) -> list[Perturbation]:
    """Parse Stage 1 LLM response into Perturbation objects."""
    span_lookup = {c.span_id: c for c in candidates}

    arr_match = re.search(r"\[.*\]", response, re.DOTALL)
    if not arr_match:
        return []

    try:
        items = json.loads(arr_match.group(0))
    except json.JSONDecodeError:
        return []

    perturbations = []
    for i, item in enumerate(items):
        span_id = item.get("span_id", "")
        if span_id not in span_lookup:
            continue

        span = span_lookup[span_id]
        perturbed = item.get("perturbed", "")
        if not perturbed or perturbed == span.text:
            continue

        try:
            category = ErrorCategory(item.get("category", ""))
        except ValueError:
            continue

        perturbations.append(Perturbation(
            perturbation_id=f"P{i:03d}_{span_id}",
            span_id=span_id,
            category=category,
            original=span.text,  # from OUR store, not the model's
            perturbed=perturbed,
            why_wrong=item.get("why_wrong", ""),
        ))

    return perturbations