---
name: repo-to-skill
description: Distill an open-source repository into an original, maintainable Agent Skill with license checks, provenance, executable helpers, and behavioral tests. Use when adapting a repository's workflow or domain knowledge; not for cosmetic rebranding or copying unlicensed material.
---

# Repository to Skill

Transform a repository's reusable operating knowledge into a small Skill while preserving attribution and adding demonstrable original value.

## Before implementation

1. Inspect the repository, its history, documentation, release state, and license. Read [references/license-gates.md](references/license-gates.md) before copying any text, code, templates, or assets.
2. Write a one-paragraph capability thesis: user request, observable output, and why a general agent would otherwise fail.
3. Create a provenance record using [references/provenance.md](references/provenance.md). Record exact upstream URLs and revisions even when only ideas are retained.
4. Classify planned content as `original`, `adapted`, or `verbatim`. Default to original instructions derived from observed behavior.

## Build

- Keep `SKILL.md` focused on routing, decisions, invariants, and the shortest successful workflow.
- Move conditional detail to `references/`; add a script only where deterministic execution improves correctness.
- Preserve the user's chosen tools and scope. Never make network writes or destructive operations implicit.
- Add at least one meaningful improvement over upstream: portability, validation, recovery, measurable quality gates, accessibility, or a new workflow - not renamed headings.
- Add realistic scenarios that test behavior and boundaries. Use `skill-benchmark` when available.

## Quality gate

Run `python scripts/check_provenance.py provenance.json` and the repository's Skill linter. Stop if the license is missing or incompatible, attribution is incomplete, or the claimed original improvement is not observable.

In the final handoff, disclose upstream inspiration, copied/adapted components, license obligations, original additions, and test evidence.
