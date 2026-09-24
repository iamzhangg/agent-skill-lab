#!/usr/bin/env python3
import argparse, json
from pathlib import Path

DIMS={"expectations","observability","control","verification","recovery","trust-safety","accessibility"}; SEV={"critical":0,"high":1,"medium":2,"low":3}
def validate(data):
    if data.get("schema_version")!="1.0": raise ValueError("schema_version must be 1.0")
    if not data.get("product") or not data.get("audience") or not data.get("journey"): raise ValueError("product, audience, and journey are required")
    if not data.get("findings"): raise ValueError("findings must not be empty")
    ids=set()
    for f in data["findings"]:
        if f["id"] in ids: raise ValueError(f"duplicate finding ID: {f['id']}")
        ids.add(f["id"])
        if f.get("dimension") not in DIMS or f.get("severity") not in SEV: raise ValueError(f"{f['id']}: invalid dimension or severity")
        for key in ("state","evidence","consequence","recommendation","acceptance_criteria"):
            if not f.get(key): raise ValueError(f"{f['id']}: {key} required")
def render(data):
    validate(data); lines=[f"# Agent UX audit: {data['product']}","",f"Audience: {data['audience']}",""]
    for f in sorted(data["findings"],key=lambda x:SEV[x["severity"]]):
        lines += [f"## [{f['severity'].upper()}] {f['id']} · {f['dimension']}","",f"- State: {f['state']}",f"- Evidence: {f['evidence']}",f"- Consequence: {f['consequence']}",f"- Recommendation: {f['recommendation']}",f"- Acceptance: {f['acceptance_criteria']}",""]
    return "\n".join(lines)
def main():
    p=argparse.ArgumentParser(); p.add_argument("command",choices=["validate","render"]); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args(); d=json.loads(a.input.read_text(encoding="utf-8")); validate(d)
    result="OK" if a.command=="validate" else render(d)
    if a.output: a.output.write_text(result+"\n",encoding="utf-8")
    else: print(result)
if __name__=="__main__": main()
