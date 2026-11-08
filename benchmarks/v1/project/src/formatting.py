"""User-facing formatting helpers."""


def normalized_person_name(value):
    if value is None:
        return ""
    return value.strip().lower()


def normalized_customer_name(value):
    if value is None:
        return ""
    return value.strip().lower()


def normalized_product_name(text):
    if text is None:
        return ""
    return text.strip().lower()


def normalized_email(value):
    if value is None:
        return ""
    return value.strip().lower()
