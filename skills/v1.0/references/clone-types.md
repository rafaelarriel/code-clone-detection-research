# Clone taxonomy (operational guide)

Use the common four-type classification as **working categories**, not a guarantee that every pair has one unambiguous label. A clone may contain nested clones of other types. Classify the largest justified meaningful span and explain ambiguity.

| Type | Interpretation | Typical clues | Caution |
|---|---|---|---|
| T1 | Identical code apart from whitespace, layout and comments | Identical token sequence after non-semantic formatting changes | Syntax-level identity does not imply the contexts are interchangeable. |
| T2 | Structurally identical code differing in identifiers, types and/or literals (as permitted by the operational definition) | Same statements/operators/control flow after consistent renaming and permitted substitutions | Different literals can alter behavior; do not automatically claim equivalent outputs. |
| T3 | Copied or similar code with added, deleted or changed statements, in addition to T1/T2 differences | Common backbone of statements with gaps or altered blocks | Inspect changed branches and error handling; not every shared scaffold is a refactoring opportunity. |
| T4 | Same computation / functionality with substantially different syntax or structure | Loop vs combinator; recursion vs iteration; differently ordered computation | This is **suspected semantic equivalence** until relevant inputs, side effects, exceptions and edge cases are considered. |

## Examples (Python)

### T1: whitespace differences
```python
def double(x):
    return x * 2

def double_copy(x):
  return x * 2
```
Function names differ here, so the complete definitions are NOT T1; the `return x * 2` statements are T1. Always classify the **exact reported span**, not the surrounding function name.

### T2: renamed identifiers
```python
def area(width, height):
    result = width * height
    return result

def product(a, b):
    value = a * b
    return value
```
May qualify as T2 after consistent renaming. Context and domain differ, so extraction is not automatically warranted.

### T3: modified sequence
```python
def total(items):
    result = 0
    for item in items:
        result += item.price
    return result

def discounted_total(items):
    result = 0
    for item in items:
        result += item.price
    result *= 0.9
    return result
```
Differences in discount policy are material; consider extracting common accumulation only.

### T4: different structure
```python
def total_loop(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

def total_builtin(numbers):
    return sum(numbers)
```
Potential T4 for suitable numeric inputs. Validate empty inputs, custom numeric types, iterator effects and exception behavior before asserting equivalence.

## Important distinctions

- **Clone** is a relation between concrete code fragments; **code smell** is an assessment of potential design problems. A clone is not necessarily a code smell in context.
- **Same purpose ≠ same semantics.** Two methods both named `validate_user` may implement different policies.
- **Same output on a few tests ≠ full equivalence.** Tests raise confidence but do not prove equivalence in general.
- Shared syntax imposed by a framework may be low-value duplication.

## Background reading (for research, not proof of an individual result)

- Roy, C. K.; Cordy, J. R.; Koschke, R. *Comparison and Evaluation of Code Clone Detection Techniques and Tools: A Qualitative Approach*. Science of Computer Programming, 2009. Verify bibliographic metadata before citing in an academic manuscript.
