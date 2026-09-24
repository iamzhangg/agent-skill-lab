---
name: agent-ux-audit
description: Audit an AI or agent product flow for expectation-setting, observability, user control, recovery, trust, safety, and accessibility, then produce evidence-linked findings and testable acceptance criteria. Use for specs, prototypes, screenshots, or journey reviews; not for generic visual critique.
---

# Agent UX Audit

Evaluate whether a person can understand, steer, verify, and recover from an AI system—not whether the interface merely looks polished.

## Workflow

1. Identify the user, consequential goal, model/tool boundaries, and irreversible actions. Map the flow from intent through execution, verification, and recovery.
2. Inspect the seven dimensions in [references/rubric.md](references/rubric.md). Evaluate actual states shown in the artifact; label assumptions when evidence is missing.
3. Record findings with stable IDs, artifact locations, severity, evidence, user consequence, recommendation, and acceptance criteria using [references/schema.md](references/schema.md).
4. Prioritize failures that combine high consequence with low detectability or weak recovery. Cosmetic consistency cannot outrank a blocked or misleading task.
5. Run `python scripts/audit.py validate audit.json`, then `python scripts/audit.py render audit.json --output audit.md`.

## Guardrails

- Do not claim model accuracy, safety, or accessibility without observable evidence.
- Distinguish “AI is working”, “AI is waiting”, “AI needs the user”, “AI failed”, and “AI completed but needs verification”.
- Require preview/confirmation for external communication, spending, deletion, permission changes, and other consequential actions.
- Recommendations must name the affected state and an acceptance test; avoid vague advice such as “make it clearer”.

## Deliverables

Return a journey map, validated `audit.json`, severity-ranked `audit.md`, and a short “first three fixes” sequence.
