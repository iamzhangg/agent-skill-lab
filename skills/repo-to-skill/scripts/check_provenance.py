#!/usr/bin/env python3
"""Check that a repository-to-skill adaptation records meaningful provenance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    record = json.loads(args.record.read_text(encoding="utf-8"))
    errors: list[str] = []
    if not record.get("project"):
        errors.append("missing project")
    if not record.get("original_contributions"):
        errors.append("missing original_contributions")
    for index, upstream in enumerate(record.get("upstreams", []), start=1):
        for field in ("url", "revision", "license", "usage", "components", "changes"):
            if not upstream.get(field):
                errors.append(f"upstream {index}: missing {field}")
        if upstream.get("usage") not in {"idea", "adapted", "verbatim"}:
            errors.append(f"upstream {index}: invalid usage")
    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors))
        return 1
    print(f"OK: {record['project']} provenance is complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
