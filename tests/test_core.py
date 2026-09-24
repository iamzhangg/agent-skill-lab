import json
import tempfile
import unittest
import subprocess
import sys
from pathlib import Path

from agent_portfolio.benchmark import grade_suite
from agent_portfolio.evidence import render_evidence_pack, validate_evidence_pack
from agent_portfolio.skill import lint_repository


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_all_skills_lint(self):
        report = lint_repository(ROOT)
        self.assertTrue(report)
        self.assertEqual({name: errors for name, errors in report.items() if errors}, {})

    def test_benchmark_example_passes(self):
        spec = json.loads((ROOT / "examples/benchmark/cases.json").read_text(encoding="utf-8"))
        results = json.loads((ROOT / "examples/benchmark/results.json").read_text(encoding="utf-8"))
        report = grade_suite(spec, results)
        self.assertTrue(report["passed"])
        self.assertEqual(report["score"], 1.0)

    def test_blocking_assertion_overrides_score(self):
        spec = {"threshold": 0.5, "cases": [{"id": "x", "assertions": [
            {"type": "contains", "value": "ok"},
            {"type": "not_contains", "value": "secret", "blocking": True},
        ]}]}
        report = grade_suite(spec, {"results": [{"id": "x", "transcript": "ok secret"}]})
        self.assertFalse(report["passed"])
        self.assertEqual(report["blocking_failures"], 1)

    def test_evidence_example_renders(self):
        pack = json.loads((ROOT / "examples/evidence/ai-skills-landscape.json").read_text(encoding="utf-8"))
        rendered = render_evidence_pack(pack)
        self.assertIn("Grade / stance", rendered)
        self.assertIn("agentskills.io", rendered)

    def test_evidence_rejects_search_snippet_url(self):
        pack = {"question": "q", "as_of": "2026-09-24", "items": [{
            "claim": "c", "url": "not-a-url", "title": "t", "publisher": "p",
            "published_at": "2026-09-24", "accessed_at": "2026-09-24",
            "tier": "D", "support": "s", "status": "context"
        }]}
        with self.assertRaisesRegex(ValueError, "HTTP"):
            validate_evidence_pack(pack)

    def test_new_skill_examples_validate(self):
        cases = [
            ("china-opportunity-radar", "radar.py", "opportunities.json"),
            ("feedback-to-prd", "feedback_prd.py", "prd.json"),
            ("agent-ux-audit", "audit.py", "audit.json"),
            ("multimodal-launch-kit", "launch.py", "launch.json"),
        ]
        for skill, script, sample in cases:
            with self.subTest(skill=skill):
                result = subprocess.run([
                    sys.executable, ROOT / "skills" / skill / "scripts" / script,
                    "validate", ROOT / "examples" / skill / sample,
                ], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
