# Architecture

The repository separates probabilistic work from deterministic checks.

1. An agent reads a small `SKILL.md` and decides which detailed reference is relevant.
2. The agent performs judgment-heavy work: decomposing a research question, identifying a license risk, or designing scenarios.
3. A local script validates the artifact's objective invariants.
4. Saved results are graded by transparent assertions and checked in CI.

This boundary keeps the model flexible where interpretation matters while making dates, required fields, local links, provenance, and release gates reproducible.

## Data flow

```text
prompt ─► Skill workflow ─► JSON/artifacts ─► validator/grader ─► Markdown report
              ▲                                      │
              └──────────── regression feedback ─────┘
```

The benchmark runner deliberately grades saved results rather than calling a model. This makes the demo offline, inexpensive, and reproducible. A production integration can add model execution adapters without changing the case or report format.
