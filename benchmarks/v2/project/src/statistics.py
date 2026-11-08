"""Simple list and iterator statistics."""

def number_above_zero(numbers):
    result = 0
    for n in numbers:
        if n > 0:
            result += 1
    return result


def number_above_zero_comprehension(numbers):
    return len([n for n in numbers if n > 0])


def number_at_least_zero(numbers):
    result = 0
    for n in numbers:
        if n >= 0:
            result += 1
    return result


def sum_elements(numbers):
    return sum(numbers)


def sum_elements_loop(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def count_even(numbers):
    return sum(1 for n in numbers if n % 2 == 0)


def count_odd(numbers):
    return sum(1 for n in numbers if n % 2 != 0)


def count_nonempty_strings(strings):
    return sum(1 for s in strings if s)
