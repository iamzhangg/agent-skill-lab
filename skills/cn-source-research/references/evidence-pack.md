# Evidence pack format

The JSON root contains `question`, `as_of`, and `items`. Each item contains:

- `claim`: atomic proposition supported by the source.
- `url`: canonical HTTP(S) URL.
- `title`, `publisher`, `published_at`, `accessed_at`. Use `null` when the original publication date is not available.
- `tier`: `A`, `B`, `C`, or `D`.
- `support`: short paraphrase of what the source establishes.
- `quote`: optional short excerpt; keep quotations minimal.
- `status`: `supports`, `contradicts`, or `context`.
- `limitations`: optional scope or methodology caveat.

Dates use `YYYY-MM-DD`. Do not place secrets, login-only content, or personal data in the pack.
