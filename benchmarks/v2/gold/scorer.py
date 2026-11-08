"""Private evaluation utility: scores manually coded case judgments; NOT a clone detector.

Usage: python scorer.py assessments.csv
CSV columns: execution,condition,model,effort,case_id,score_0_1,detected_0_1,type_correct_0_1,notes
Judgments must be completed by evaluator; blank scores are excluded, never assumed zero.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Uso: python scorer.py FORMULARIO-AVALIACAO.csv")
seen = set()
data = defaultdict(list)
with Path(sys.argv[1]).open(encoding="utf-8-sig", newline="") as file:
    for row in csv.DictReader(file):
        execution = row["execution"].strip()
        case = row["case_id"].strip()
        score = row["score_0_1"].strip()
        if not execution or not score:
            continue
        key = (execution, case)
        if key in seen:
            raise ValueError(f"duplicated score row: {key}")
        seen.add(key)
        if score not in ("0", "1"):
            raise ValueError(f"score must be 0 or 1: {key}")
        data[(execution, row["condition"], "positive" if case.startswith("P") else "negative-nonassertion")].append(int(score))
for (execution, condition, kind), values in sorted(data.items()):
    print(f"{execution:12} {condition:12} {kind:23} {sum(values)}/{len(values)} = {sum(values)/len(values):.1%}")
