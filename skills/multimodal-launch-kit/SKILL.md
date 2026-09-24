---
name: multimodal-launch-kit
description: Turn a product brief, article, transcript, or user-owned demo video into a launch narrative, timestamped shot plan, bilingual channel copy, and validated asset manifest. Use for product launches and demo repurposing; not for downloading unlicensed media or fabricating product claims.
---

# Multimodal Launch Kit

Build a coherent product launch system from source material while preserving the line between demonstrated capability and marketing claim.

## Workflow

1. Confirm the audience, launch goal, channels, language, call to action, and ownership or permission for supplied media.
2. Extract a claim inventory from the source. Mark each claim as demonstrated, sourced, planned, or unsupported; unsupported claims do not enter final copy.
3. Choose one narrative spine—problem-to-outcome, before/after, proof walkthrough, or use-case montage—using [references/narratives.md](references/narratives.md).
4. Create timestamped clips and assets in the manifest format from [references/schema.md](references/schema.md). Every asset needs a source reference, channel, aspect ratio, and status.
5. Adapt the message for each channel rather than truncating one master caption. Preserve the same factual claim set.
6. Run `python scripts/launch.py validate launch.json`, then `python scripts/launch.py render launch.json --output launch-plan.md`.

## Guardrails

- Do not download, clip, or redistribute media without permission or a valid basis.
- Never imply a feature is live when the source labels it planned, mocked, or experimental.
- Captions, subtitles, and translated claims must preserve numbers, limitations, and uncertainty.
- Treat platform dimensions and duration limits as configurable release data, not timeless facts; verify them before a real launch.
- Obtain confirmation before posting, messaging, uploading, or spending money.

## Deliverables

Return validated `launch.json`, `launch-plan.md`, a claim ledger, a shot list, channel copy, and a missing-assets checklist. This Skill plans and validates; media rendering remains an explicit downstream action.
