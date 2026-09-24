# PRD schema

Use `schema_version: "1.0"`, `title`, `decision`, `feedback`, `themes`, and `requirements`.

Feedback requires `id`, `text`, `source`, and `segment`. Requirements require `id`, `title`, non-empty `evidence_ids`, `outcome`, `success_metric`, `non_goals`, and RICE fields: numeric `reach`, `impact`, `confidence` in 0–1, and positive `effort`.

The deterministic score is `reach × impact × confidence ÷ effort`; it sorts hypotheses but does not decide strategy.
