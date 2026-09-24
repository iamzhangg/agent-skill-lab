# Launch schema

Use `schema_version: "1.0"`, `product`, `audience`, `goal`, `claims`, and `assets`.

Claims require `id`, `text`, `status` (`demonstrated`, `sourced`, `planned`, or `unsupported`) and `source`. Assets require `id`, `channel`, `format`, `aspect_ratio`, `source_refs`, `claim_ids`, `status` (`ready`, `planned`, or `blocked`), and optional numeric `start_seconds`/`end_seconds` where end must be greater than start.
