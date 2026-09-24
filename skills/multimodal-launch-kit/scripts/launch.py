#!/usr/bin/env python3
import argparse, json
from pathlib import Path

STATUSES={"demonstrated","sourced","planned","unsupported"}; ASSET={"ready","planned","blocked"}
def validate(data):
    if data.get("schema_version")!="1.0": raise ValueError("schema_version must be 1.0")
    claims={c["id"]:c for c in data.get("claims",[])}
    if not claims or not data.get("assets"): raise ValueError("claims and assets must not be empty")
    for c in claims.values():
        if c.get("status") not in STATUSES or not c.get("source"): raise ValueError(f"{c['id']}: invalid status or missing source")
    for a in data["assets"]:
        if a.get("status") not in ASSET or not a.get("channel") or not a.get("aspect_ratio") or not a.get("source_refs"): raise ValueError(f"{a['id']}: incomplete asset")
        unknown=set(a.get("claim_ids",[]))-set(claims)
        if unknown: raise ValueError(f"{a['id']}: unknown claims {sorted(unknown)}")
        if any(claims[x]["status"]=="unsupported" for x in a.get("claim_ids",[])): raise ValueError(f"{a['id']}: unsupported claim used")
        if "start_seconds" in a and float(a.get("end_seconds",0))<=float(a["start_seconds"]): raise ValueError(f"{a['id']}: invalid timestamps")
def render(data):
    validate(data); lines=[f"# Launch plan: {data['product']}","",f"Audience: {data['audience']}  ",f"Goal: {data['goal']}","","## Claim ledger",""]
    lines += [f"- `{c['status']}` {c['text']} — {c['source']}" for c in data["claims"]]
    lines += ["","## Assets",""]
    for a in data["assets"]: lines += [f"### {a['id']} · {a['channel']}","",f"- Format: {a['format']} / {a['aspect_ratio']}",f"- Status: {a['status']}",f"- Claims: {', '.join(a.get('claim_ids',[])) or 'none'}",""]
    return "\n".join(lines)
def main():
    p=argparse.ArgumentParser(); p.add_argument("command",choices=["validate","render"]); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args(); d=json.loads(a.input.read_text(encoding="utf-8")); validate(d)
    result="OK" if a.command=="validate" else render(d)
    if a.output: a.output.write_text(result+"\n",encoding="utf-8")
    else: print(result)
if __name__=="__main__": main()
