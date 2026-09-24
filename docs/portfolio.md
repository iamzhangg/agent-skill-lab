# Portfolio talking points

## Portfolio narrative

The portfolio now follows one AI product lifecycle: find an evidence-backed opportunity, synthesize user feedback, specify the experience, audit agent trust states, plan a truthful launch, and prove behavior with regression tests. Two interactive labs make the product decisions visible without requiring an API key.

## The problem

Agent Skills are easy to publish but hard to trust. A strong portfolio should demonstrate where the agent may improvise, where deterministic code should take over, and how failures become regression tests.

## Engineering decisions

- Standard-library-only core: reviewers can run the project immediately and audit every check.
- Blocking assertions: a safety or authorization failure cannot be hidden by a high average score.
- Explicit provenance: reuse is an engineering input, not a branding shortcut.
- Chinese-source specialization: platform signals, repost chains, geographic scope, and freshness are treated as first-class risks.

## Honest limitations

- The included runner grades completed transcripts; it does not execute an LLM.
- Source tiers guide judgment but cannot replace domain expertise.
- License gates are an engineering checklist, not legal advice.
- The example evidence pack demonstrates the format and contains only claims supported by linked public pages; it is not a comprehensive market report.

## Interview walkthrough

1. Start with `china-opportunity-radar` to show signal judgment and falsifiable discovery.
2. Use `feedback-to-prd` to trace requirements to evidence instead of generating a generic PRD.
3. Use `agent-ux-audit` and Agent Trust Lab to discuss autonomy, verification, and recovery.
4. Close with AI Feature Tradeoff Lab and `skill-benchmark` to show prioritization and measurable quality.

## Suggested next milestones

1. Add adapters for Codex and Claude Code execution traces.
2. Add repeated-run variance and an optional calibrated LLM judge.
3. Publish benchmark history as a small static dashboard.
4. Replace one synthetic case with an anonymized, permissioned case from a target employer domain.
