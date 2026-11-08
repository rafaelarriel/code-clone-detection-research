# Evidence-first, two-pass inspection

1. List examined source files. Mark unscanned files. Ignore generated, vendored, and binary content unless explicitly in scope.
2. Build a conceptual function inventory across modules: loops, folds, filters, validations, formatting, mapping, pipelines, error paths. Read enough code to confirm real spans.
3. Compare candidates by literal chunks, consistent renamings, near-miss edits, and alternative operations. **Do not stop at the first representative of a group**: check all members and missed candidates, including an extra function under an unrelated name.
4. For each group, inspect pairs at **body versus definition** scope. If more than two members, list members and identify all pertinent pair distinctions without inflating independent group counts.
5. Before final output perform a negative/near-miss pass: boundary conditions (`>` vs `>=`), empty inputs, normalization, stable ordering, exception behavior, short one-liners, side effects, truthiness, iterators, numeric types.
6. Keep `structural finding`, `semantic claim`, and `recommendation` as separate fields.
7. Confidence must concern classification/detection evidence, **not an invented numeric probability**. High/medium/low with explanation.

Short, valid structural matches may be moved to a `low-value/trivial` appendix with locations and classification, rather than erased. Do not include them in an 'actionable clone' tally by default.

When reports are long, prioritize the most significant groups, but disclose truncation and unreported candidates. Do not claim exhaustive pairwise comparison without the necessary reads.
