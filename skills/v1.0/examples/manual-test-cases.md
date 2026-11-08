# Manual smoke-test cases (NOT a benchmark)

Use this file as a didactic prompt to inspect the skill's classification and refusal to overclaim. Line numbers below are illustrative only and do not refer to real project files.

## Case A — exact statement (T1 on selected line, not necessarily whole function)
```python
def first(x):
    return x * 2

def second(x):
    return x * 2
```
Expected: repeated `return` statements are T1; full function definitions have different names and may instead be T2.

## Case B — renamed (T2)
```python
def measure(a, b):
    result = a * b
    return result

def compute(x, y):
    product = x * y
    return product
```
Expected: T2 candidate, but do not automatically recommend abstraction across unrelated domains.

## Case C — gapped logic (T3)
```python
def amount(lines):
    total = 0
    for line in lines:
        total += line.price
    return total

def amount_discount(lines):
    total = 0
    for line in lines:
        total += line.price
    if total >= 100:
        total -= 10
    return total
```
Expected: T3 candidate; changed business rule must remain explicit.

## Case D — semantic candidate (T4)
```python
def s1(nums):
    return sum(nums)

def s2(nums):
    total = 0
    for n in nums:
        total += n
    return total
```
Expected: suspected T4, not unqualified equivalence across arbitrary types and iterators.

## Case E — false positive
```python
def has_permission(user):
    return user.role == 'admin'

def is_admin_dashboard_visible(user):
    return user.role == 'admin'
```
Expected: same expression is a structural clone, but could be intentional; no automatic extraction or assertion that the domain policy should be unified.

## Case F — near-similarity NOT equivalent
```python
def avg(values):
    return sum(values) / len(values)

def total(values):
    return sum(values)
```
Expected: common syntax does not establish T4 equivalence. Note division and empty-list behavior.
