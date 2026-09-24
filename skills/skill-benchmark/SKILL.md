---
name: skill-benchmark
description: Design and run lightweight behavioral evaluations for Agent Skills using realistic scenarios, observable assertions, boundary cases, and regression reports. Use when proving a Skill works or comparing revisions; not for judging prose style from a single cherry-picked example.
---

# Skill benchmark

Turn a Skill's promises into repeatable evidence. Prefer a few discriminating scenarios over many shallow examples.

## Design

1. Extract capabilities and boundaries from the Skill description and body.
2. Define a balanced suite: happy path, ambiguous input, missing prerequisite, unsafe or out-of-scope request, and regression case when applicable.
3. Make assertions observable. Supported deterministic assertions are documented in [references/case-format.md](references/case-format.md).
4. Keep fixtures free of secrets and network dependencies. Separate the prompt/fixture from the expected behavior so test data does not leak the answer.

## Execute

Run each scenario in a clean workspace with the target Skill and save the final transcript or artifact manifest. Then grade it:

```bash
python scripts/grade.py cases.json results.json --output report.md
```

Do not silently rewrite failing expectations to match the latest output. Diagnose whether the failure belongs to the Skill, evaluator, fixture, or environment.

## Interpret

- Report assertion-level results, not just a single score.
- Treat safety and authorization failures as blocking even if the aggregate score is high.
- Distinguish deterministic checks from model-judged rubrics. If using an LLM judge, record model, prompt, temperature, and repeated-run variance.
- A benchmark demonstrates behavior under its scenarios; it does not prove universal reliability.

Use [references/reporting.md](references/reporting.md) for the final summary and regression decision.
