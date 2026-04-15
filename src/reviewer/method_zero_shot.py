"""Method 1: Zero-shot paper review."""

from datetime import date
import json
import re

from .client import chat
from .models import ReviewResult
from .prompts import ZERO_SHOT_CHUNK_PROMPT, OCR_CAVEAT, ZERO_SHOT_PROMPT, FIELD_INFORMATION
from .utils import assign_paragraph_indices, chunk_text, count_tokens, parse_review_response

MAX_TOKENS_SINGLE = 100_000  # use single prompt if paper fits


def review_zero_shot(
    paper_slug: str,
    document_content: str,
    model: str = "anthropic/claude-opus-4-6",
    reasoning_effort: str | None = None,
    ocr: bool = False,
) -> ReviewResult:
    # get field information
    prompt = FIELD_INFORMATION.format(paper_start=document_content[:2000])
    response, usage = chat(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        max_tokens=256,
        reasoning_effort=reasoning_effort,
    )
    
    text = re.sub(r"^```(?:json)?\s*", "", response.strip())
    text = re.sub(r"\s*```$", "", text).strip()
    field_result = json.loads(text)
    field_information = f"{field_result['field']} ({field_result['subfield']}). Pay particular attention to {', '.join(field_result['pitfalls'])}"

    # review
    result = ReviewResult(method="zero_shot", paper_slug=paper_slug, model=model,
                          reasoning_effort=reasoning_effort)

    token_count = count_tokens(document_content)

    if token_count <= MAX_TOKENS_SINGLE:
        ocr_caveat = OCR_CAVEAT if ocr else ""
        prompt = ZERO_SHOT_PROMPT.format(paper_text=document_content, field_information=field_information, current_date=date.today().isoformat(), ocr_caveat=ocr_caveat)
        response, usage = chat(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            max_tokens=8192,
            reasoning_effort=reasoning_effort,
        )
        result.raw_responses.append(response)
        result.total_prompt_tokens += usage["prompt_tokens"]
        result.total_completion_tokens += usage["completion_tokens"]
        overall, comments = parse_review_response(response)
        result.overall_feedback = overall
        result.comments = comments
    else:
        # Chunked approach
        chunks = chunk_text(document_content, max_tokens=80_000)
        all_comments = []
        overall_parts = []
        for i, chunk in enumerate(chunks):
            ocr_caveat = OCR_CAVEAT if ocr else ""
            prompt = ZERO_SHOT_CHUNK_PROMPT.format(
                chunk_num=i + 1,
                total_chunks=len(chunks),
                chunk_text=chunk,
                field_information=field_information,
                current_date=date.today().isoformat(),
                ocr_caveat=ocr_caveat,
            )
            response, usage = chat(
                messages=[{"role": "user", "content": prompt}],
                model=model,
                max_tokens=8192,
                reasoning_effort=reasoning_effort,
            )
            result.raw_responses.append(response)
            result.total_prompt_tokens += usage["prompt_tokens"]
            result.total_completion_tokens += usage["completion_tokens"]
            overall, comments = parse_review_response(response)
            if overall:
                overall_parts.append(overall)
            all_comments.extend(comments)
        result.overall_feedback = "\n\n".join(overall_parts)
        result.comments = all_comments

    assign_paragraph_indices(result.comments, document_content)
    return result
