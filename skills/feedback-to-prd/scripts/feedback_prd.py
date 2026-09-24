#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path

def normalize(path):
    if path.suffix.lower()==".json": rows=json.loads(path.read_text(encoding="utf-8-sig"))
    elif path.suffix.lower()==".csv":
        with path.open(encoding="utf-8-sig", newline="") as f: rows=list(csv.DictReader(f))
    else: rows=[{"text": x.strip()} for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    return [{"id": str(r.get("id") or f"F{i:03}"), "text": str(r.get("text") or r.get("feedback") or "").strip(), "source": str(r.get("source") or "unknown"), "segment": str(r.get("segment") or "unknown")} for i,r in enumerate(rows,1)]

def validate(data):
    if data.get("schema_version")!="1.0": raise ValueError("schema_version must be 1.0")
    feedback={x["id"] for x in data.get("feedback",[]) if x.get("text")}
    if not feedback: raise ValueError("feedback must not be empty")
    if not data.get("requirements"): raise ValueError("requirements must not be empty")
    for r in data["requirements"]:
        if not r.get("evidence_ids") or set(r["evidence_ids"])-feedback: raise ValueError(f"{r['id']}: evidence IDs must resolve")
        if not r.get("outcome") or not r.get("success_metric") or not r.get("non_goals"): raise ValueError(f"{r['id']}: outcome, success_metric, and non_goals required")
        if not 0 <= float(r.get("confidence",-1)) <= 1 or float(r.get("effort",0)) <= 0: raise ValueError(f"{r['id']}: invalid RICE values")

def score(r): return float(r["reach"])*float(r["impact"])*float(r["confidence"])/float(r["effort"])
def render(data):
    validate(data); lines=[f"# {data['title']}","",f"**Decision:** {data['decision']}",""]
    for r in sorted(data["requirements"], key=score, reverse=True):
        lines += [f"## {r['title']} · RICE {score(r):.2f}","",f"- Evidence: {', '.join(r['evidence_ids'])}",f"- Outcome: {r['outcome']}",f"- Success: {r['success_metric']}",f"- Non-goals: {'; '.join(r['non_goals'])}",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(); p.add_argument("command",choices=["normalize","validate","render"]); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    data=normalize(a.input) if a.command=="normalize" else json.loads(a.input.read_text(encoding="utf-8"))
    if a.command=="validate": validate(data); result="OK"
    elif a.command=="render": result=render(data)
    else: result=json.dumps(data,ensure_ascii=False,indent=2)
    if a.output: a.output.write_text(result+("\n" if not result.endswith("\n") else ""),encoding="utf-8")
    else: print(result)
if __name__=="__main__": main()
