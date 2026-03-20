"""Utilities for parsing reviewer output and chunking text."""

import json
import re
from difflib import SequenceMatcher

import tiktoken

from .models import Comment


def _get_encoding():
    """Get a tiktoken encoding for approximate token counting."""
    try:
        return tiktoken.get_encoding("o200k_base")
    except Exception:
        return None


def count_tokens(text: str) -> int:
    enc = _get_encoding()
    if enc is None:
        return len(text) // 4
    return len(enc.encode(text))


def truncate_text(text: str, max_tokens: int) -> str:
    """Truncate text to at most max_tokens tokens."""
    enc = _get_encoding()
    if enc is None:
        return text[: max_tokens * 4]
    tokens = enc.encode(text)[:max_tokens]
    return enc.decode(tokens)


def chunk_text(text: str, max_tokens: int = 6000, overlap_tokens: int = 200) -> list[str]:
    """Split text into chunks of at most max_tokens with overlap."""
    try:
        enc = tiktoken.get_encoding("cl100k_base")
    except Exception:
        chars_per_chunk = max_tokens * 4
        overlap_chars = overlap_tokens * 4
        chunks = []
        i = 0
        while i < len(text):
            chunks.append(text[i : i + chars_per_chunk])
            i += chars_per_chunk - overlap_chars
        return chunks

    tokens = enc.encode(text)
    chunks = []
    i = 0
    while i < len(tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunks.append(enc.decode(chunk_tokens))
        i += max_tokens - overlap_tokens
    return chunks


def split_into_paragraphs(text: str, min_chars: int = 100) -> list[str]:
    """Split document into paragraphs, merging short ones with the next."""
    raw = [p.strip() for p in text.split("\n\n") if p.strip()]
    paragraphs: list[str] = []
    carry = ""
    for p in raw:
        if carry:
            p = carry + "\n\n" + p
            carry = ""
        if len(p) < min_chars:
            carry = p
        else:
            paragraphs.append(p)
    if carry:
        if paragraphs:
            paragraphs[-1] = paragraphs[-1] + "\n\n" + carry
        else:
            paragraphs.append(carry)
    return paragraphs


# Maps for math normalization — built once at import time.
_UNICODE_MATH_MAP = {
    "\u2264": "<=",   # ≤
    "\u2265": ">=",   # ≥
    "\u2260": "!=",   # ≠
    "\u2261": "=",    # ≡
    "\u2248": "~",    # ≈
    "\u221e": "inf",  # ∞
    "\u2211": "sum",  # ∑
    "\u220f": "prod", # ∏
    "\u222b": "int",  # ∫
    "\u2202": "d",    # ∂
    "\u2207": "nabla",# ∇
    "\u22a4": "T",    # ⊤
    "\u22a5": "T",    # ⊥
    "\u03b1": "alpha", "\u03b2": "beta", "\u03b3": "gamma",
    "\u03b4": "delta", "\u03b5": "epsilon", "\u03b6": "zeta",
    "\u03b7": "eta", "\u03b8": "theta", "\u03b9": "iota",
    "\u03ba": "kappa", "\u03bb": "lambda", "\u03bc": "mu",
    "\u03bd": "nu", "\u03be": "xi", "\u03c0": "pi",
    "\u03c1": "rho", "\u03c3": "sigma", "\u03c4": "tau",
    "\u03c5": "upsilon", "\u03c6": "phi", "\u03c7": "chi",
    "\u03c8": "psi", "\u03c9": "omega",
    "\u0393": "gamma", "\u0394": "delta", "\u0398": "theta",
    "\u039b": "lambda", "\u039e": "xi", "\u03a0": "pi",
    "\u03a3": "sigma", "\u03a6": "phi", "\u03a8": "psi",
    "\u03a9": "omega",
    "\u210b": "h",    # ℋ
    "\u2112": "l",    # ℒ
    "\u2115": "n",    # ℕ
    "\u211d": "r",    # ℝ
    "\U0001d49e": "c",  # 𝒞
    "\U0001d4b0": "u",  # 𝒰
    "\U0001d4b2": "w",  # 𝒲
    "\U0001d7cf": "1",  # 𝟏 (bold 1)
    "\u2061": "",     # invisible function application
    "\u200b": "",     # zero-width space
    "\u200c": "",     # zero-width non-joiner
    "\u200d": "",     # zero-width joiner
    "\u00d7": "x",   # ×
    "\u22c5": ".",    # ⋅
    "\u2026": "...",  # …
    "\u27e8": "(",    # ⟨
    "\u27e9": ")",    # ⟩
    "\u2016": "||",   # ‖
    "\u2032": "'",    # ′
    "\u2019": "'",    # right single quote
    "\u201c": '"',    # left double quote
    "\u201d": '"',    # right double quote
    "\u2013": "-",    # en dash
    "\u2014": "-",    # em dash
    "\u2018": "'",    # left single quote
}

_LATEX_SYMBOL_MAP = {
    "\\leq": "<=", "\\geq": ">=", "\\neq": "!=", "\\approx": "~",
    "\\equiv": "=", "\\sim": "~", "\\propto": "~",
    "\\infty": "inf", "\\partial": "d",
    "\\nabla": "nabla", "\\forall": "forall", "\\exists": "exists",
    "\\in": "in", "\\notin": "notin", "\\subset": "subset",
    "\\supset": "supset", "\\cup": "cup", "\\cap": "cap",
    "\\times": "x", "\\cdot": ".", "\\ldots": "...", "\\cdots": "...",
    "\\top": "T", "\\bot": "T",
    "\\sum": "sum", "\\prod": "prod", "\\int": "int",
    "\\log": "log", "\\exp": "exp", "\\sin": "sin", "\\cos": "cos",
    "\\tan": "tan", "\\max": "max", "\\min": "min", "\\sup": "sup",
    "\\inf": "inf", "\\lim": "lim", "\\arg": "arg",
    "\\alpha": "alpha", "\\beta": "beta", "\\gamma": "gamma",
    "\\delta": "delta", "\\epsilon": "epsilon", "\\varepsilon": "epsilon",
    "\\zeta": "zeta", "\\eta": "eta", "\\theta": "theta",
    "\\vartheta": "theta", "\\iota": "iota", "\\kappa": "kappa",
    "\\lambda": "lambda", "\\mu": "mu", "\\nu": "nu", "\\xi": "xi",
    "\\pi": "pi", "\\rho": "rho", "\\sigma": "sigma",
    "\\varsigma": "sigma", "\\tau": "tau", "\\upsilon": "upsilon",
    "\\phi": "phi", "\\varphi": "phi", "\\chi": "chi",
    "\\psi": "psi", "\\omega": "omega",
    "\\Gamma": "gamma", "\\Delta": "delta", "\\Theta": "theta",
    "\\Lambda": "lambda", "\\Xi": "xi", "\\Pi": "pi",
    "\\Sigma": "sigma", "\\Phi": "phi", "\\Psi": "psi", "\\Omega": "omega",
    "\\langle": "(", "\\rangle": ")",
    "\\lVert": "||", "\\rVert": "||", "\\|": "||",
    "\\left": "", "\\right": "", "\\big": "", "\\Big": "",
    "\\bigg": "", "\\Bigg": "",
}

# Regex to extract content from \command{content} style LaTeX
_LATEX_WRAPPED_CMD_RE = re.compile(
    r"\\(?:operatorname|mathrm|mathbf|mathbb|mathcal|mathit|mathsf|mathtt"
    r"|text|textbf|textit|mbox|boldsymbol|overline|underline"
    r"|hat|tilde|bar|vec|dot|ddot|widetilde|widehat)\{([^}]*)\}"
)


def _normalize_math(text: str) -> str:
    """Strip LaTeX commands and Unicode math so both forms reduce to plain tokens."""
    # Unicode math symbols -> ASCII equivalents
    for u, a in _UNICODE_MATH_MAP.items():
        text = text.replace(u, a)
    # Strip remaining non-ASCII symbols (catches math operators we didn't map)
    text = re.sub(r"[^\x00-\x7f]", " ", text)

    # LaTeX: remove spacing commands
    text = re.sub(r"\\[;,!: ]", " ", text)
    text = re.sub(r"\\(?:quad|qquad|hspace|vspace|hfill|vfill)\b\{?[^}]*\}?", " ", text)
    # LaTeX: \command{content} -> content
    text = _LATEX_WRAPPED_CMD_RE.sub(r" \1 ", text)
    # LaTeX: named symbols -> word equivalents
    for latex, repl in _LATEX_SYMBOL_MAP.items():
        text = text.replace(latex, " " + repl + " ")
    # Remove remaining LaTeX commands (e.g. \frac, \sqrt, unknown ones)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    # Remove braces, carets, backslashes
    text = re.sub(r"[{}\\^~]", " ", text)
    return text


def _normalize_for_match(text: str) -> str:
    """Normalize extracted text for quote-to-paragraph matching."""
    text = text.lower()
    text = text.replace("<br>", " ")
    text = text.replace("|", " ")
    text = text.replace("*", "")
    text = _normalize_math(text)
    text = text.replace("_", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _quote_coverage(quote: str, window: str) -> float:
    """Fraction of the quote covered by matching blocks in the window.

    Unlike ``SequenceMatcher.ratio()`` which divides by the combined length
    of both strings, this divides only by the quote length so that extra
    content in the window does not penalise the score.
    """
    if not quote:
        return 0.0
    sm = SequenceMatcher(None, quote, window, autojunk=False)
    matched = sum(block.size for block in sm.get_matching_blocks())
    return matched / len(quote)


def locate_comment_in_document(
    quote: str,
    paragraphs: list[str],
    threshold: float = 0.3,
) -> int | None:
    """Find the paragraph index that best matches a quote.

    Uses fuzzy substring matching. Returns the index of the best-matching
    paragraph, or None if no paragraph scores above *threshold*.
    """
    if not quote or not paragraphs:
        return None

    quote_norm = _normalize_for_match(quote)[:1000]
    best_idx = None
    best_score = 0.0

    for i, para in enumerate(paragraphs):
        para_norm = _normalize_for_match(para)
        # Fast exact-substring check first
        if quote_norm and quote_norm in para_norm:
            return i

        # Compare against sliding windows so long table-like paragraphs still match.
        if len(para_norm) <= len(quote_norm) + 200:
            windows = [para_norm]
        else:
            window_size = min(len(para_norm), max(len(quote_norm) + 200, 400))
            step = max(window_size // 2, 100)
            windows = [
                para_norm[start : start + window_size]
                for start in range(0, len(para_norm) - window_size + 1, step)
            ]
            if (len(para_norm) - window_size) % step:
                windows.append(para_norm[-window_size:])

        score = max(_quote_coverage(quote_norm, window) for window in windows)
        if score > best_score:
            best_score = score
            best_idx = i

    return best_idx if best_score >= threshold else None


def assign_paragraph_indices(
    comments: list[Comment],
    document_content: str,
) -> None:
    """Set paragraph_index on each comment by locating its quote in the document."""
    paragraphs = split_into_paragraphs(document_content)
    for comment in comments:
        comment.paragraph_index = locate_comment_in_document(
            comment.quote, paragraphs
        )


def parse_comments_from_list(items: list[dict]) -> list[Comment]:
    """Convert a list of raw dicts into Comment objects."""
    comments = []
    for item in items:
        if not isinstance(item, dict):
            continue
        title = item.get("title", item.get("name", "Untitled"))
        quote = item.get("quote", item.get("flagged_text", item.get("text", "")))
        explanation = item.get("explanation", item.get("message", item.get("comment", "")))
        comment_type = item.get("type", item.get("comment_type", "logical")).lower()
        if comment_type not in ("technical", "logical"):
            comment_type = "technical" if any(
                kw in (title + explanation).lower()
                for kw in ["formula", "equation", "math", "proof", "calculation",
                           "theorem", "incorrect", "wrong", "error", "sign", "factor",
                           "variance", "derivation", "typo", "parameter"]
            ) else "logical"
        paragraph_index = item.get("paragraph_index", None)
        if paragraph_index is not None:
            paragraph_index = int(paragraph_index)
        comments.append(Comment(
            title=title,
            quote=quote,
            explanation=explanation,
            comment_type=comment_type,
            paragraph_index=paragraph_index,
        ))
    return comments


def _decode_jsonish_string(value: str) -> str:
    """Best-effort decode of a JSON-style string fragment."""
    def _unicode_repl(match):
        try:
            return chr(int(match.group(1), 16))
        except ValueError:
            return match.group(0)

    value = re.sub(r"\\u([0-9a-fA-F]{4})", _unicode_repl, value)
    value = value.replace(r"\/", "/")
    value = value.replace(r"\"",
                          "\"")
    value = value.replace(r"\n", "\n")
    value = value.replace(r"\r", "\r")
    value = value.replace(r"\t", "\t")
    value = value.replace(r"\\", "\\")
    return value


def _extract_overall_feedback_fallback(text: str) -> str:
    """Recover overall_feedback from malformed JSON-ish output."""
    match = re.search(
        r'"overall_feedback"\s*:\s*"(?P<value>.*?)"\s*,\s*"comments"\s*:',
        text,
        re.DOTALL,
    )
    if not match:
        return ""
    return _decode_jsonish_string(match.group("value")).strip()


def _extract_comments_fallback(text: str) -> list[Comment]:
    """Recover comment objects from malformed JSON-ish output.

    This is intentionally schema-specific and only targets the comment shape
    emitted by our prompts: title, quote, explanation, type.
    """
    pattern = re.compile(
        r'\{\s*"title"\s*:\s*"(?P<title>.*?)"\s*,\s*'
        r'"quote"\s*:\s*"(?P<quote>.*?)"\s*,\s*'
        r'"explanation"\s*:\s*"(?P<explanation>.*?)"\s*,\s*'
        r'"type"\s*:\s*"(?P<type>technical|logical)"\s*\}',
        re.DOTALL,
    )
    items = []
    for match in pattern.finditer(text):
        items.append({
            "title": _decode_jsonish_string(match.group("title")).strip(),
            "quote": _decode_jsonish_string(match.group("quote")).strip(),
            "explanation": _decode_jsonish_string(match.group("explanation")).strip(),
            "type": match.group("type").strip(),
        })
    return parse_comments_from_list(items)


def parse_review_response(response: str) -> tuple[str, list[Comment]]:
    """Parse LLM response returning (overall_feedback, comments).

    Handles two formats:
    - {"overall_feedback": "...", "comments": [...]}  (preferred)
    - [...]  (bare array fallback)
    """
    # Try to extract first valid JSON object or array using raw_decode
    text = response.strip()
    # Strip markdown code fences if present
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = text.strip()

    decoder = json.JSONDecoder()
    obj = None
    # Scan for the first parseable top-level object/array
    for i, ch in enumerate(text):
        if ch in ("{", "["):
            try:
                candidate, _ = decoder.raw_decode(text, i)
            except json.JSONDecodeError:
                continue
            if isinstance(candidate, list):
                if not candidate or isinstance(candidate[0], dict):
                    obj = candidate
                    break
                continue
            if isinstance(candidate, dict) and (
                "overall_feedback" in candidate or "comments" in candidate
            ):
                obj = candidate
                break
    else:
        # Nothing parseable found
        return _extract_overall_feedback_fallback(text), _extract_comments_fallback(text)

    if isinstance(obj, dict):
        overall_feedback = obj.get("overall_feedback", "")
        items = obj.get("comments", [])
        return overall_feedback, parse_comments_from_list(items)
    elif isinstance(obj, list):
        return "", parse_comments_from_list(obj)
    return _extract_overall_feedback_fallback(text), _extract_comments_fallback(text)


def parse_comments_from_response(response: str) -> list[Comment]:
    """Parse a JSON array of comments from an LLM response (legacy wrapper)."""
    _, comments = parse_review_response(response)
    return comments
