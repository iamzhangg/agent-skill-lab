"""A deterministic, transparent assertion runner for saved agent results."""

from __future__ import annotations

import re
from typing import Any


def _json_path(data: Any, path: str) -> Any:
    current = data
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def _check(assertion: dict, result: dict) -> tuple[bool, str]:
    transcript = result.get("transcript", "")
    kind = assertion.get("type")
    expected = assertion.get("value")
    if kind == "contains":
        ok = str(expected).casefold() in transcript.casefold()
    elif kind == "not_contains":
        ok = str(expected).casefold() not in transcript.casefold()
    elif kind == "regex":
        ok = re.search(str(expected), transcript, flags=re.IGNORECASE | re.MULTILINE) is not None
    elif kind == "file_exists":
        ok = expected in result.get("files", [])
    elif kind == "json_path":
        ok = _json_path(result.get("data", {}), assertion.get("path", "")) == expected
    else:
        return False, f"unknown assertion type: {kind}"
    return ok, f"{kind}={expected!r}"


def grade_suite(spec: dict, results: dict) -> dict:
    by_id = {item["id"]: item for item in results.get("results", [])}
    details: list[dict] = []
    passed_count = total = 0
    blocking_failures = 0
    for case in spec.get("cases", []):
        result = by_id.get(case["id"], {})
        checks = []
        for assertion in case.get("assertions", []):
            total += 1
            ok, label = _check(assertion, result)
            passed_count += int(ok)
            if not ok and assertion.get("blocking", False):
                blocking_failures += 1
            checks.append({"passed": ok, "label": label, "blocking": assertion.get("blocking", False)})
        details.append({"id": case["id"], "checks": checks})
    threshold = float(spec.get("threshold", 1.0))
    score = passed_count / total if total else 0.0
    return {
        "suite": spec.get("suite", "unnamed"), "score": score,
        "passed_assertions": passed_count, "total_assertions": total,
        "blocking_failures": blocking_failures,
        "passed": score >= threshold and blocking_failures == 0,
        "details": details,
    }


def render_report(report: dict) -> str:
    mark = "PASS" if report["passed"] else "FAIL"
    lines = [f"# Benchmark: {report['suite']}", "", f"**{mark}** — {report['passed_assertions']}/{report['total_assertions']} assertions ({report['score']:.0%}); {report['blocking_failures']} blocking failures.", ""]
    for case in report["details"]:
        lines.append(f"## {case['id']}")
        for check in case["checks"]:
            symbol = "✅" if check["passed"] else "❌"
            blocking = " (blocking)" if check["blocking"] else ""
            lines.append(f"- {symbol} `{check['label']}`{blocking}")
        lines.append("")
    return "\n".join(lines)
