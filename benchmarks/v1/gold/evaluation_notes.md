# Suggested evaluation protocol (pilot only)

1. Save the exact agent model/version, prompting mode, skill version, project checksum and run date.
2. For a baseline, run the prompt in `project/README.md` *without* the skill in a fresh session. In a second fresh session, rerun with skill access, keeping other factors controlled.
3. Do not expose any files under `ground-truth/` to the agent in either condition.
4. Compare findings to the 9 annotated pairs. Count TP only if the pair is correctly localized (function + file), and separately record correctness of type and line span. For Type 1 check **body scope**.
5. For T4, verify reported input-domain assumptions. A pure name/structure match is not enough. Review Type 4 negatives independently.
6. Do not treat novel unannotated pairs as automatic FP; adjudicate them and update a frozen labeled corpus for later experiments.
7. For robust precision/recall/F1, develop a comprehensively labeled test corpus with multiple annotators, blind review, frozen evaluation scope, plus multiple runs and statistical analysis. This mini-project alone cannot justify generalization.
8. Suggested record: experiment_id, agent, model, skill_condition, run_id, group_id, found, correct_type, correct_location, false_positive_review, comments.

## Interpreting two subtle cases

- `N04` and `N05` are NOT absolute non-clones: their similar structure may legitimately be flagged as near-duplicates (T2/T3). They should simply **not** be described as semantically equivalent Type 4 pairs.
- `G01` and `G06` are Type 1 body clones (without function declaration); comparing full function definitions yields Type 2 because function names differ.
