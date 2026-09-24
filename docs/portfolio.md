# Portfolio talking points

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

## Suggested next milestones

1. Add adapters for Codex and Claude Code execution traces.
2. Add repeated-run variance and an optional calibrated LLM judge.
3. Publish benchmark history as a small static dashboard.
4. Add a fourth Skill that solves a domain problem from an actual target employer.
