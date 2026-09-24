---
name: cn-source-research
description: Research claims across the Chinese web with source grading, freshness checks, cross-source verification, and a reusable evidence pack. Use for China-market, Chinese-language, or mixed Chinese/English research; not for casual browsing or unsupported trend summaries.
---

# Chinese-source research

Produce a decision-ready answer whose claims can be traced back to dated sources. Optimize for evidence quality, not link count.

## Workflow

1. Restate the decision, audience, geography, and time horizon. Treat words such as "latest", "popular", and "best" as time-sensitive.
2. Turn the question into 3-7 claims that could be proven wrong. Search in Chinese and, where useful, English.
3. Grade candidates with [references/source-grading.md](references/source-grading.md). Prefer primary sources; do not use reposts to corroborate their originals.
4. For consequential claims, seek either one authoritative primary source or two genuinely independent sources. Record disagreement instead of averaging it away.
5. Capture each retained item in the evidence-pack format described in [references/evidence-pack.md](references/evidence-pack.md).
6. Run `python scripts/render_evidence.py evidence.json --output evidence.md`. Fix validation errors before drafting.
7. Write the synthesis with dates, scope, uncertainty, and citations adjacent to the supported claims. Separate sourced facts from inference.

## Guardrails

- Never treat search snippets, AI summaries, screenshots, or unattributed social posts as final evidence.
- Preserve Chinese names and technical terms; add an English gloss only when it helps the audience.
- Do not infer national adoption from a single city, platform, or creator community.
- A platform metric is not a market metric. Label views, likes, sales, registrations, and active users precisely.
- If a page is inaccessible, cite an accessible original or omit the claim; do not cite a second-hand quote as if verified.

## Deliverables

Return a concise synthesis plus the validated `evidence.json` and rendered `evidence.md`. Include a "known unknowns" section when evidence is incomplete or conflicting.
