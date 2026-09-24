#!/usr/bin/env python3
import argparse, json, math
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

SCORES = ("evidence_strength", "user_value", "feasibility", "strategic_fit")

def validate(data):
    if data.get("schema_version") != "1.0": raise ValueError("schema_version must be 1.0")
    date.fromisoformat(data["as_of"])
    if not data.get("decision"): raise ValueError("decision is required")
    evidence = {x["id"]: x for x in data.get("evidence", [])}
    if not evidence: raise ValueError("evidence must not be empty")
    for item in evidence.values():
        if urlparse(item["url"]).scheme not in {"http", "https"}: raise ValueError(f"invalid evidence URL: {item['id']}")
        date.fromisoformat(item["accessed_at"])
        if item["tier"] not in "ABCD": raise ValueError(f"invalid tier: {item['id']}")
    if not data.get("opportunities"): raise ValueError("opportunities must not be empty")
    for item in data["opportunities"]:
        missing = set(item.get("evidence_ids", [])) - set(evidence)
        if missing: raise ValueError(f"{item['id']}: unknown evidence IDs {sorted(missing)}")
        if not item.get("evidence_ids") or not item.get("disconfirming_test"): raise ValueError(f"{item['id']}: evidence and disconfirming_test required")
        for key in SCORES:
            if not isinstance(item.get(key), int) or not 1 <= item[key] <= 5: raise ValueError(f"{item['id']}: {key} must be 1..5")

def render(data):
    validate(data)
    lines = ["# Opportunity radar / 机会雷达", "", f"**Decision / 决策：** {data['decision']}", f"**As of / 截止：** {data['as_of']}", ""]
    ranked = sorted(data["opportunities"], key=lambda x: -math.prod(x[k] for k in SCORES))
    for item in ranked:
        score = math.prod(item[k] for k in SCORES)
        lines += [f"## {item['title']} — {score}", "", f"**JTBD:** When {item['context']}, {item['user']} needs {item['job']}, but {item['barrier']}, so they can {item['outcome']}.", f"**Evidence:** {', '.join(item['evidence_ids'])}", f"**Risks:** {'; '.join(item.get('risks', [])) or 'None recorded'}", f"**Disconfirming test:** {item['disconfirming_test']}", ""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(); p.add_argument("command", choices=["validate","render"]); p.add_argument("input", type=Path); p.add_argument("--output", type=Path); a=p.parse_args()
    data=json.loads(a.input.read_text(encoding="utf-8")); validate(data)
    if a.command=="render":
        result=render(data)
        if a.output: a.output.write_text(result, encoding="utf-8")
        else: print(result)
    else: print("OK")
if __name__ == "__main__": main()
