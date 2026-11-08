# Human-only evaluation materials — DO NOT expose to agent

- `gold_labels.json`: annotated expected pairs, with line spans and caveats.
- `labels.csv`: compact pair table for manual comparison.
- `evaluation_notes.md`: scoring guidance and method caveats.

**Important:** The sample intentionally includes multiple valid structural overlaps and unclear granularity. Positive examples are *expected detections*, not an exhaustive gold standard of every clone pair. A finding absent from the key must be reviewed by a human, not automatically marked as a false positive. “Negative” pairs are only negative for *Type 4 semantic equivalence*, and may be Type 2/3 clones.

Use `scope` while interpreting Type 1: the equality is in the function *body*, since the function declarations use different names. If a tool compares whole definitions, classify those cases as Type 2.
