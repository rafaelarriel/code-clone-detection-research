# Research evaluation protocol (proposed; not experimental results)

## Question
Does an instruction-only Agent Skill improve clone detection and refactoring assessments relative to the **same** coding agent without the skill?

## Controlled setup

- Compare baseline (same agent, no skill) to skill condition (same agent with skill). Optionally compare a second agent as a separate factor.
- Fix repository commit, model version (where selectable), access to tools, time/token budget, user task prompt, languages and report format. To isolate instructions, give the baseline the same output schema and scope but **not** the skill's technical detection procedures.
- Use identical held-out code samples and human-reviewed ground-truth clone pairs / non-clones. Include T1–T4, negative examples and boundary cases. Do not use examples from skill documentation as the only evaluation set.
- Randomize condition order or start clean sessions to reduce contamination; repeat runs where feasible and record variability.
- Blind human reviewers to the condition when rating output quality; document disagreements and adjudication.

## Measures

- Detection: TP, FP, FN under a predeclared matching rule for fragment spans / pair identity; precision = TP/(TP+FP); recall = TP/(TP+FN); F1 = 2PR/(P+R). Define handling of overlapping clone groups, duplicates and ambiguous ground truth before testing.
- Stratify results by clone type. Report Type 4 separately due to semantic ambiguity and benchmark coverage.
- Refactoring: expert rubric for behavioral preservation, appropriateness of abstraction, actionability, tests/edge cases and risk awareness; identify whether checks were actually executed.
- Operational: tokens, time, analysis coverage, run-to-run agreement, if reliably measurable.

## Threats to validity

- Construct: ambiguous definitions of T3/T4 and ground truth; precision depends on span-matching rules.
- Internal: prompt leakage, different context/tools, order effects, stochastic sampling.
- External: selected languages, codebases, sample size, model/harness support and difficulty distribution.
- Conclusion: small samples and assessor bias; report confidence intervals or uncertainty where appropriate.

## Integrity

Never fabricate metrics or test outcomes. The skill's examples are demonstration cases, not evidence of predictive performance. Record failures, unsupported conclusions and omitted files.
