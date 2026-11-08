# Safe refactoring recommendations

A clone is not automatically a defect. Favor maintaining separate implementations when semantics, ownership, evolution rates, dependencies or security boundaries differ.

## Refactoring options

- **Extract function/method** for a stable, cohesive repeated algorithm.
- **Parameterize variation** when the same algorithm differs only in a genuine policy parameter; avoid boolean-flag explosion.
- **Extract shared module/service** when ownership and dependency direction permit it.
- **Template Method / Strategy** only when behavior genuinely varies along a stable interface; avoid overengineering.
- **Keep duplication** when expected divergence, different domain meaning, performance, test isolation or coupling cost outweigh benefits.

## Required reasoning

For every proposal, state:
1. Which fragment(s) to consolidate and the proposed common responsibility.
2. Which differences must remain explicit and why.
3. Preconditions for equivalence (types, edge cases, errors, ordering, side effects).
4. Expected benefit and risks (coupling, dependencies, readability, performance, regressions).
5. Regression checks: unit/property tests, boundary cases and integration tests relevant to visible code.
6. Whether the recommendation is illustrative or validated; never claim tests passed unless executed and results observed.

For T4, prefer proposing **characterization tests first**, then refactor only after observational equivalence is adequately supported. If there is no reliable way to preserve behavior, recommend no refactoring.

## Output constraints

Provide a concise plan or pseudocode only; no wholesale patches unless specifically requested. Never make edits silently. Review security-sensitive code especially conservatively (auth, permissions, money, cryptography, concurrency, persistence).
