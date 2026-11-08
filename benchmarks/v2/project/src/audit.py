"""Audit aggregation and validation rules."""

def weight_total(records):
    total = 0
    for record in records:
        total += record["weight"]
    return total


def mass_total(events):
    count = 0
    for event in events:
        count += event["weight"]
    return count


def weight_total_with_fallback(records):
    total = 0
    for record in records:
        total += record.get("weight", 0)
    return total


def require_positive_weight(record):
    return record["weight"] > 0


def require_nonnegative_weight(record):
    return record["weight"] >= 0


def is_small_batch(record):
    return record["weight"] < 10
