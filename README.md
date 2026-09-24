# Agent Skill Lab / 智能体技能实验室

[![CI](https://github.com/iamzhangg/agent-skill-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/iamzhangg/agent-skill-lab/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

一套面向真实工作的 Agent Skills 与评测工具。重点不是“收藏提示词”，而是把研究、开源改造和行为评测变成可追踪、可测试、可回归的工程流程。

An original, bilingual portfolio of production-minded Agent Skills. Each Skill couples concise agent instructions with deterministic tooling, provenance, and test evidence.

## Why this repository

多数 Skill 只能展示一段漂亮的指令。本项目刻意补齐三个常被忽略的环节：中文互联网的信源质量、开源二次开发的许可证与溯源、Agent 行为的可重复验证。

| Skill | Real-world problem | Verifiable output |
|---|---|---|
| [`cn-source-research`](skills/cn-source-research/SKILL.md) | 中文与中国市场研究容易混用转载、平台热度和过期信息 | 分级、带日期、可渲染的 evidence pack |
| [`repo-to-skill`](skills/repo-to-skill/SKILL.md) | “改装开源 Skill”容易沦为换皮或遗漏许可证 | provenance record + license gate + original-value check |
| [`skill-benchmark`](skills/skill-benchmark/SKILL.md) | Skill 的效果常靠截图和单次演示证明 | 场景化断言、阻断项、机器可读评分报告 |

## 60-second demo

No runtime dependencies are required.

```bash
python -m pip install -e .
skill-lab lint .
skill-lab evidence examples/evidence/ai-skills-landscape.json
skill-lab benchmark examples/benchmark/cases.json examples/benchmark/results.json
python -m unittest discover -s tests -v
```

Every Skill also ships a standalone script, so it can be copied into Codex, Claude Code, Cursor, or another Agent Skills-compatible environment without installing the package.

## Design principles

```text
User intent
   │
   ▼
small SKILL.md ──► conditional references
   │                       │
   ▼                       ▼
deterministic scripts ──► inspectable artifacts
   │
   ▼
behavioral benchmark + CI
```

- Progressive disclosure: routing and invariants stay in `SKILL.md`; deep detail loads only when needed.
- Evidence over vibes: outputs have schemas, dates, assertions, and failure modes.
- Honest adaptation: inspiration and licenses are visible in [`PROVENANCE.md`](PROVENANCE.md).
- Portable by default: Python standard library only; no API key required for the demo.

## Repository map

```text
skills/       installable Agent Skills
src/          shared zero-dependency validation and evaluation library
examples/     evidence packs and benchmark fixtures
tests/        unit tests for success and failure behavior
docs/         architecture and portfolio talking points
```

## Install a Skill

Copy one folder into your agent's supported skills directory. For Codex, for example:

```bash
cp -r skills/cn-source-research ~/.codex/skills/
```

Paths differ by agent and version; follow the current documentation for your client.

## Portfolio notes

See [`docs/portfolio.md`](docs/portfolio.md) for interview-ready explanations of the engineering decisions, limitations, and next milestones.

## Credits and license

The packaging philosophy was informed by public Agent Skills work in the Chinese and global open-source communities, including projects by [归藏 / op7418](https://github.com/op7418). No upstream Skill text, styles, or assets are redistributed here. Exact research notes and distinctions between inspiration and implementation are recorded in [`PROVENANCE.md`](PROVENANCE.md).

Code and original documentation in this repository are released under the [MIT License](LICENSE).
