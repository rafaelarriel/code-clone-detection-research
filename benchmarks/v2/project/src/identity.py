"""Normalization and identity handling."""

def clean_contact(value):
    if value is None:
        return ""
    return value.strip().lower()


def clean_supplier(value):
    if value is None:
        return ""
    return value.strip().lower()


def clean_document(text):
    if text is None:
        return ""
    return text.strip().lower()


def clean_city(city):
    if city is None:
        return ""
    return city.strip().lower()


def clean_upper(value):
    if value is None:
        return ""
    return value.strip().upper()


def clean_contact_casefold(value):
    if value is None:
        return ""
    return value.strip().casefold()


def clean_contact_without_strip(value):
    if value is None:
        return ""
    return value.lower()
