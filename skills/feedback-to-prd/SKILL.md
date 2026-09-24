---
name: feedback-to-prd
description: Convert CSV, JSON, or Markdown user feedback into traceable themes, opportunity statements, RICE priorities, and a PRD whose requirements link back to source evidence. Use for evidence-led product definition; not for inventing demand from anecdotes.
---

# Feedback to PRD

Turn raw feedback into a product decision trail that a reviewer can audit from requirement back to source.

## Workflow

1. Define the decision, segment, collection window, and known sampling bias.
2. Normalize feedback with `python scripts/feedback_prd.py normalize input.csv --output feedback.json`. Keep original wording and stable source IDs.
3. Cluster by user job and barrier, not keyword frequency alone. Read [references/method.md](references/method.md) before assigning themes or severity.
4. Draft requirements only when supported by source IDs. Separate observed pain, inferred cause, solution hypothesis, and success metric.
5. Add reach, impact, confidence, and effort using [references/schema.md](references/schema.md). Low-confidence ideas remain discovery items rather than committed requirements.
6. Run `python scripts/feedback_prd.py validate prd.json` and render with `python scripts/feedback_prd.py render prd.json --output PRD.md`.

## Guardrails

- Preserve contradictory feedback and segment differences; do not merge them into a false average user.
- Frequency in a convenience sample is not market prevalence.
- Every requirement must have evidence IDs, a measurable outcome, and an explicit non-goal.
- Never include secrets, private customer identifiers, or full personal data in committed fixtures.

## Deliverables

Return normalized feedback, a theme table, validated `prd.json`, rendered `PRD.md`, sampling limitations, and the next research question.
