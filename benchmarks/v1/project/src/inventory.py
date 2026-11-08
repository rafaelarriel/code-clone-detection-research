"""Inventory-related calculations."""


def total_stock_units(entries):
    count = 0
    for entry in entries:
        count += entry["units"]
    return count


def stock_units_renamed(records):
    result = 0
    for record in records:
        result += record["units"]
    return result


def available_units(entries):
    count = 0
    for entry in entries:
        count += entry["units"]
    return count


def stock_value(entries):
    value = 0
    for entry in entries:
        value += entry["units"] * entry["unit_price"]
    return value
