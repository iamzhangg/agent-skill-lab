"""Command-line entry point."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .benchmark import grade_suite, render_report
from .evidence import render_evidence_pack
from .skill import lint_repository


def main() -> int:
    parser = argparse.ArgumentParser(prog="skill-lab")
    sub = parser.add_subparsers(dest="command", required=True)
    lint = sub.add_parser("lint", help="validate all skills")
    lint.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    evidence = sub.add_parser("evidence", help="validate and render evidence JSON")
    evidence.add_argument("input", type=Path)
    benchmark = sub.add_parser("benchmark", help="grade saved results")
    benchmark.add_argument("cases", type=Path)
    benchmark.add_argument("results", type=Path)
    args = parser.parse_args()

    if args.command == "lint":
        report = lint_repository(args.root)
        for name, errors in report.items():
            print(f"{'OK' if not errors else 'FAIL'} {name}")
            for error in errors:
                print(f"  - {error}")
        return int(any(report.values()))
    if args.command == "evidence":
        print(render_evidence_pack(json.loads(args.input.read_text(encoding="utf-8"))))
        return 0
    spec = json.loads(args.cases.read_text(encoding="utf-8"))
    results = json.loads(args.results.read_text(encoding="utf-8"))
    report = grade_suite(spec, results)
    print(render_report(report))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
