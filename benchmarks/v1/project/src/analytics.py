"""Data summary routines."""


def positive_count(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += 1
    return result


def positives_len(numbers):
    return len([number for number in numbers if number > 0])


def count_nonnegative(numbers):
    result = 0
    for number in numbers:
        if number >= 0:
            result += 1
    return result


def total_sum(numbers):
    return sum(numbers)


def manual_total_sum(numbers):
    acc = 0
    for number in numbers:
        acc += number
    return acc


def average(numbers):
    return sum(numbers) / len(numbers)
