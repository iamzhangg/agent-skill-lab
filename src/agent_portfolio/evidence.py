"""Validation and Markdown rendering for evidence packs."""

from __future__ import annotations

from datetime import date
from urllib.parse import urlparse


REQUIRED_ROOT = ("question", "as_of", "items")
REQUIRED_ITEM = (
    "claim", "url", "title", "publisher", "accessed_at",
    "tier", "support", "status",
)


def _date(value: str, field: str) -> None:
    try:
        date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must use YYYY-MM-DD") from exc


def validate_evidence_pack(pack: dict) -> None:
    for field in REQUIRED_ROOT:
        if field not in pack:
            raise ValueError(f"missing root field: {field}")
    _date(pack["as_of"], "as_of")
    if not isinstance(pack["items"], list) or not pack["items"]:
        raise ValueError("items must be a non-empty list")
    for index, item in enumerate(pack["items"], start=1):
        for field in REQUIRED_ITEM:
            if field not in item or item[field] in (None, ""):
                raise ValueError(f"item {index}: missing {field}")
        parsed = urlparse(item["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"item {index}: url must be HTTP(S)")
        if item["tier"] not in {"A", "B", "C", "D"}:
            raise ValueError(f"item {index}: invalid tier")
        if item["status"] not in {"supports", "contradicts", "context"}:
            raise ValueError(f"item {index}: invalid status")
        if item.get("published_at") is not None:
            _date(item["published_at"], f"item {index}.published_at")
        _date(item["accessed_at"], f"item {index}.accessed_at")


def render_evidence_pack(pack: dict) -> str:
    validate_evidence_pack(pack)
    lines = [f"# Evidence: {pack['question']}", "", f"As of: {pack['as_of']}", ""]
    for index, item in enumerate(pack["items"], start=1):
        lines.extend([
            f"## {index}. {item['claim']}", "",
            f"- Source: [{item['title']}]({item['url']}) — {item['publisher']}",
            f"- Published / accessed: {item.get('published_at') or 'unknown'} / {item['accessed_at']}",
            f"- Grade / stance: {item['tier']} / {item['status']}",
            f"- Support: {item['support']}",
        ])
        if item.get("limitations"):
            lines.append(f"- Limitations: {item['limitations']}")
        if item.get("quote"):
            lines.append(f"> {item['quote']}")
        lines.append("")
    return "\n".join(lines)
