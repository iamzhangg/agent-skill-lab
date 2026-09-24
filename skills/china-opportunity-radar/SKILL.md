---
name: china-opportunity-radar
description: Turn Chinese-market signals into evidence-backed product opportunities with freshness, independence, JTBD, signal-strength, and validation checks. Use for China-focused opportunity discovery or product strategy; not for unsupported trend lists or investment advice.
---

# China Opportunity Radar

Convert scattered market signals into falsifiable product opportunities. The output is a decision aid, not a prediction.

## Workflow

1. Lock the audience, geography, decision, and `as_of` date. Reject “China users” as a segment until it is narrowed to observable behavior.
2. Gather claims with `cn-source-research` when available. Distinguish adoption, intent, attention, and revenue; never combine them into one “popularity” metric.
3. Normalize retained evidence using [references/schema.md](references/schema.md). Record the original URL, date, source tier, and whether sources are independent.
4. Frame opportunities as `When [context], [user] needs [job], but [barrier], so they can [outcome]`. Score evidence strength separately from product attractiveness using [references/scoring.md](references/scoring.md).
5. Add the cheapest disconfirming test for every opportunity. Mark weak, stale, single-platform, or contradictory evidence explicitly.
6. Run `python scripts/radar.py validate opportunities.json`, then `python scripts/radar.py render opportunities.json --output opportunity-brief.md`.

## Guardrails

- Do not present search volume, views, registrations, active use, willingness to pay, and revenue as interchangeable.
- Do not infer a national trend from one city, platform, creator, or repost chain.
- Never score an opportunity without at least one evidence ID and one disconfirming test.
- Keep sourced facts, interpretation, and recommendation visibly separate.
- If the decision could cause material financial loss, describe further research needed rather than recommending an investment.

## Deliverables

Return the validated `opportunities.json`, a bilingual-ready `opportunity-brief.md`, and the evidence pack used. Include “Why now”, “Why this may be noise”, and “What would change the decision”.
