# Behavioral equivalence and refactoring safeguards

Before recommending reuse, check input domain, outputs, errors, side effects, mutation, call ordering, data types, concurrency, numeric precision, resource use, business semantics and external observability.

- Different thresholds, discounts, VAT rules, inclusive boundaries, rounding and case folding often make behavior different **even where structures match**.
- Comprehensions vs loops may differ in allocations, iteration timing and exceptional custom protocols.
- `sum` and manual addition can differ with specialized numeric objects.
- Dictionary access with `.get()` differs from direct indexing when keys are absent.
- Stable vs unstable sorting, deduplicating vs preserving duplicates, Unicode operations, time zone or locale can matter.
- When behavior is not established: **semantic clone hypothesis** only; propose counterexample tests.

Refactor assessment independent of clone type:
* Suggest extraction only when shared domain policy, behavior-preserving API, manageable coupling, and test coverage justify it.
* Keep duplication when domain evolution, contracts, divergent invariants or readability favor independence.
* Never execute modifications or tests without permission; never assert observed test success based on hypothetical tests.
