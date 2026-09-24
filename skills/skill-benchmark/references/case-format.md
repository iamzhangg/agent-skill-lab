# Case format

`cases.json` contains a `suite` and `cases`. Each case has `id`, `prompt`, and `assertions`.

Supported assertions:

- `contains`: transcript contains a case-insensitive substring.
- `not_contains`: transcript does not contain a case-insensitive substring.
- `regex`: regular expression matches the transcript.
- `file_exists`: path appears in the result's `files` list.
- `json_path`: dot-separated path in the result's `data` equals `value`.

An assertion may set `blocking: true`. A failed blocking assertion makes the suite fail regardless of weighted score. Keep prompts realistic and never put the expected phrase in the prompt if that would make the check trivial.
