# Taxonomy, precedence, and granularity

- T1: same code except for whitespace/layout/comments. Renaming identifiers (even a function name) means the *complete function* is no longer T1; its body may still be T1 if textually identical.
- T2: same syntax with consistent identifier/type/literal substitutions (where accepted by the chosen conventional definition). Record whether a substituted literal changes behavior. A code match may be T2 even when values differ: **not semantic equivalence**.
- T3: near-miss clone with additional, removed, or modified statements in an otherwise recognizably copied structure. Differing comparison operators or branches can affect output. Do not call every shared `return` or `if` a meaningful clone.
- T4: same intended computation but structurally dissimilar implementations. Treat as semantic *hypothesis*, not proof; compare behavior on edge cases, failures, and side effects.

Granularity examples (synthetic, not from any benchmark):
```
def first(x):
    v = x * 2
    return v

def second(x):
    v = x * 2
    return v
```
Body spans are T1; complete functions are T2 due to function-name substitution.
```
def alpha(values):
    result = 0
    for v in values:
        result += v
    return result

def beta(records):
    acc = 0
    for item in records:
        acc += item
    return acc
```
Full functions are T2 through renaming.

**Precedence**: classify the exact reported spans, NOT the whole pair by a single label chosen for convenience. If body=T1 and function=T2, state both. If a shared core is T1/T2 within a T3 function pair, state both levels. For counting distinct pairs, count the routine pair once unless the benchmark explicitly evaluates multiple scope labels.

**Abstain rather than overclaim**: similarity and refactorability are separate. Functions with equal *shape* but different rules are structural clones, not interchangeable implementations.
