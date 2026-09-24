"""Static checks for portable Agent Skill folders."""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        return {}, text
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values, parts[2]


def lint_skill(path: Path) -> list[str]:
    errors: list[str] = []
    entry = path / "SKILL.md"
    if not entry.is_file():
        return ["missing SKILL.md"]
    text = entry.read_text(encoding="utf-8")
    meta, body = _frontmatter(text)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != path.name or not NAME_RE.fullmatch(name):
        errors.append("frontmatter name must match the kebab-case folder name")
    if len(description) < 40:
        errors.append("description is too short to route reliably")
    if "TODO" in text or "[TODO" in text:
        errors.append("unfinished TODO marker")
    if len(body.strip()) < 200:
        errors.append("instruction body is too short")
    for target in LINK_RE.findall(body):
        if "://" in target or target.startswith("#"):
            continue
        clean = target.split("#", 1)[0]
        candidate = path.joinpath(*PurePosixPath(clean).parts)
        if not candidate.exists():
            errors.append(f"broken local link: {target}")
    return errors


def lint_repository(root: Path) -> dict[str, list[str]]:
    skills_dir = root / "skills"
    return {
        folder.name: lint_skill(folder)
        for folder in sorted(skills_dir.iterdir())
        if folder.is_dir()
    }
