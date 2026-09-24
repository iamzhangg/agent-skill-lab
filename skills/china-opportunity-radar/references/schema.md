# Opportunity schema

The root object uses `schema_version: "1.0"`, an ISO `as_of` date, a non-empty `decision`, `evidence`, and `opportunities`.

Each evidence item requires `id`, `claim`, `url`, `publisher`, `accessed_at`, `tier` (`A`–`D`), and `metric_type` (`attention`, `intent`, `adoption`, `retention`, `revenue`, or `context`).

Each opportunity requires `id`, `title`, `user`, `context`, `job`, `barrier`, `outcome`, non-empty `evidence_ids`, integer scores from 1–5 for `evidence_strength`, `user_value`, `feasibility`, and `strategic_fit`, plus `risks` and a non-empty `disconfirming_test`.
