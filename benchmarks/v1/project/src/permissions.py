"""Permissions tests; superficially alike but behavior differs."""


def is_adult(age):
    return age >= 18


def is_minor(age):
    return age < 18


def is_positive(value):
    return value > 0


def is_nonnegative(value):
    return value >= 0


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0
