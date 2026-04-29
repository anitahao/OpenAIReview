"""LLM-based error generation from candidate spans.
"""

import json
import re

from reviewer.client import chat
from .models import (
    CandidateSpan,
    Error,
    Perturbation,
)

errors = [
    Error.NUMERIC_PARAMETER,
    Error.OPERATOR_OR_SIGN,
    Error.INDEX_OR_SUBSCRIPT,
    Error.COMPUTATION,

    Error.INCORRECT_CLAIM,

    Error.MISSING_CASE,
    Error.INDUCTION,
    Error.CIRCULAR_REASONING,
    Error.INVALID_IMPLICATION,

    Error.MISINTERP,
    Error.CAUSAL_REVERSED,
    Error.P_HACKING
]

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

FIELD_PROMPT = r"""
This is the abstract of an academic paper: 
{abstract}

Identify its main field of study and return ONLY 1-5 words. 
"""

DOMAIN_PROMPT = r"""
This is the abstract of an academic paper in {field}:
{abstract}

What are the 5 most realistic and detectable errors an author could make in this kind of paper?

Return a JSON array of 5 strings, each describing one error type concisely.

Example format:
["error type one", "error type two", "error type three", "error type four", "error type five"]

Return ONLY the JSON array. No markdown, no explanation.
"""

THEORETICAL_PROMPT = r"""
You are generating MEANINGFUL perturbations for an academic paper in the field of {field} to benchmark LLM reviewers.

While generating perturbations, consider the following possible errors:
{domain_specific}

Aim for 1 perturbation for each candidate. 

Choose from the following perturbation CANDIDATES:
{candidates_json}

If "error_type" is "surface", generate ONE compatible perturbation:
- numeric_parameter: change a numeric constant (e.g. 0.5 becomes 0.25, n=10 becomes n=100)
- operator_or_sign: flip an operator or sign (e.g. + becomes -, ≤ becomes ≥)                                               
- index_or_subscript: change a subscript/superscript (e.g. x_i becomes x_{{i+1}})                                           
- computation: introduce an arithmetic error in a derivation step

If "error_type" is "claim", generate ONE compatible perturbation:
- incorrect_claim: corrupt the statement subtly (e.g. wrong condition, wrong quantifier, wrong bound, wrong constant, wrong sign, wrong index/subscript)

If "error_type" is "logic", generate ONE compatible perturbation:
- missing_case: remove one case from case analysis, or corrupt the base case in an induction
- induction: make the inductive step invalid                                                                          
- circular_reasoning: use the theorem being proved as a step in its own proof
- invalid_implication: reverse or invalidate a key logical implication
- numeric_parameter: change a numeric constant (e.g. 0.5 becomes 0.25, n=10 becomes n=100)
- operator_or_sign: flip an operator or sign (e.g. + becomes -, ≤ becomes ≥)                                               
- index_or_subscript: change a subscript/superscript (e.g. x_i becomes x_{{i+1}})                                           
- computation: introduce an arithmetic error in a derivation step

OUTPUT FORMAT:
For each perturbation, return:
- span_id: the candidate's span_id (copy exactly)
- error: the corresponding error from {errors}
- perturbed: modified LaTeX text (must differ from original)
- why_wrong: a short explanation of how the error can be detected using ONLY the paper

Return ONLY a JSON array of perturbation objects. No commentary.

STRICT REQUIREMENTS:
- The perturbed text must be valid LaTeX
- The error must be verifiable from the paper text alone (no external knowledge)
"""

EXPERIMENTAL_PROMPT = r"""
You are generating MEANINGFUL perturbationsfor an academic paper in the field of {field} to benchmark LLM reviewers.

While generating perturbations, consider the following possible errors:
{domain_specific}

Aim for 1 perturbation for each candidate. 

Choose from the following perturbation CANDIDATES:
{candidates_json}

If "error_type" is "surface", generate ONE compatible perturbation:
- numeric_parameter: change a numeric constant (e.g. 0.5 becomes 0.25, n=10 becomes n=100)
- operator_or_sign: flip an operator or sign (e.g. + becomes -, ≤ becomes ≥)                                               
- index_or_subscript: change a subscript/superscript (e.g. x_i becomes x_{{i+1}})                                           
- computation: introduce an arithmetic error in a derivation step

If "error_type" is "claim", generate ONE compatible perturbation:
- incorrect_claim: corrupt the statement so it is factually incorrect

If "error_type" is "experimental", generate ONE compatible perturbation:
- misinterp: misinterpret a result (e.g. p-value or confidence interval)
- causal_reversed: flip a causal claim (X causes Y becomes Y causes X)                                                      
- p_hacking: introduce a methodological flaw that constitutes p-hacking (e.g. remove or negate a multiple testing correction, change the stopping rule, 
selectively report only the significant outcome from a set of tested hypotheses)
- numeric_parameter: change a numeric constant (e.g. 0.5 becomes 0.25, n=10 becomes n=100)
- operator_or_sign: flip an operator or sign (e.g. + becomes -, ≤ becomes ≥)                                               
- index_or_subscript: change a subscript/superscript (e.g. x_i becomes x_{{i+1}})                                           
- computation: introduce an arithmetic error in a derivation step

OUTPUT FORMAT:
For each perturbation, return:
- span_id: the candidate's span_id (copy exactly)
- error: the corresponding error from {errors}
- perturbed: modified LaTeX text (must differ from original)
- why_wrong: a short explanation of how the error can be detected using ONLY the paper

Return ONLY a JSON array of perturbation objects. No commentary.

STRICT REQUIREMENTS:
- The perturbed text must be valid LaTeX
- The error must be verifiable from the paper text alone (no external knowledge)
"""
# ---------------------------------------------------------------------------
# Generate perturbations:
# ---------------------------------------------------------------------------

def identify_field(abstract, model: str = "anthropic/claude-opus-4-6", reasoning_effort: str | None = None):
    formatted_prompt = FIELD_PROMPT.format(
        abstract=abstract,
    )

    response, usage = chat(
        messages=[{"role": "user", "content": formatted_prompt}],
        model=model,
        max_tokens=8192,
        reasoning_effort=reasoning_effort,
    )
    
    return response.strip().lower()

def domain_specific_errors(field, abstract, model: str = "anthropic/claude-opus-4-6", reasoning_effort: str | None = None):
    formatted_prompt = DOMAIN_PROMPT.format(
        field=field,
        abstract=abstract,
    )

    response, usage = chat(
        messages=[{"role": "user", "content": formatted_prompt}],
        model=model,
        max_tokens=8192,
        reasoning_effort=reasoning_effort,
    )

    cleaned = re.sub(r"^```[a-z]*\n?|\n?```$", "", response.strip(), flags=re.MULTILINE)
    items = json.loads(cleaned)
    return ", ".join(str(x) for x in items)

def generate_perturbations(category,
                           abstract,
                           candidates: list[CandidateSpan],
                           model: str = "anthropic/claude-opus-4-6",
                           reasoning_effort: str | None = None) -> list[Perturbation]:
    # Build candidate JSON for the prompt
    candidates_json = json.dumps([
        {
            "span_id": c.span_id,
            "text": c.text,
            "context": c.context,
            "error_type": c.error_type,
            "compatible_errors": [error.value for error in c.compatible_errors],
        }
        for c in candidates
    ], indent=2)

    field = identify_field(abstract, model=model, reasoning_effort=reasoning_effort)
    domain_specific = domain_specific_errors(field, abstract, model=model, reasoning_effort=reasoning_effort)

    if category == "theoretical":
        prompt = THEORETICAL_PROMPT
    elif category == "experimental":
        prompt = EXPERIMENTAL_PROMPT

    formatted_prompt = prompt.format(
        field=field,
        domain_specific=domain_specific,
        candidates_json=candidates_json,
        errors=", ".join(c.value for c in errors),
    )

    print(f"  {len(candidates)} candidates...")

    response, usage = chat(
        messages=[{"role": "user", "content": formatted_prompt}],
        model=model,
        max_tokens=8192,
        reasoning_effort=reasoning_effort,
    )

    perturbations = _parse_response(response, candidates)
    print(f"    -> {len(perturbations)} perturbations")

    return perturbations

# ---------------------------------------------------------------------------
# Helpers:
# ---------------------------------------------------------------------------

def _parse_response(response: str,
                    candidates: list[CandidateSpan]) -> list[Perturbation]:
    span_lookup = {c.span_id: c for c in candidates}

    # Find all valid JSON arrays in the response using the JSON decoder directly.
    # This handles nested brackets, LaTeX, and self-corrections correctly.
    # We take the last non-empty list found (model may self-correct mid-response).
    decoder = json.JSONDecoder()
    found = []
    i = 0
    while i < len(response):
        if response[i] == "[":
            try:
                obj, end = decoder.raw_decode(response, i)
                if isinstance(obj, list) and obj:
                    found.append(obj)
                i = end
            except json.JSONDecodeError:
                i += 1
        else:
            i += 1

    if not found:
        return []
    items = found[-1]

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
            error = Error(item.get("error", ""))
        except ValueError:
            continue

        perturbations.append(Perturbation(
            perturbation_id=f"P{i:03d}_{span_id}",
            span_id=span_id,
            error=error,
            original=span.text,
            offset=span.offset,  # from OUR store, not the model's
            perturbed=perturbed,
            why_wrong=item.get("why_wrong", ""),
        ))

    return perturbations