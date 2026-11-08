"""Billing routines for an illustrative application."""


def invoice_subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def invoice_subtotal_copy(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def calculate_order_value(products):
    amount = 0
    for product in products:
        amount += product["price"] * product["quantity"]
    return amount


def invoice_subtotal_with_fee(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    if total > 100:
        total += 5
    return total


def sum_net_prices(items):
    return sum(item["price"] * item["quantity"] for item in items)


def invoice_total_with_tax(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total * 1.2
