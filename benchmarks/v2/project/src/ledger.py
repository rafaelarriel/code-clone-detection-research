"""Example operations on financial records."""

def net_amount(lines):
    amount = 0
    for line in lines:
        amount += line["unit_cost"] * line["units"]
    return amount


def net_amount_copy(lines):
    amount = 0
    for line in lines:
        amount += line["unit_cost"] * line["units"]
    return amount


def invoice_base(rows):
    subtotal = 0
    for row in rows:
        subtotal += row["unit_cost"] * row["units"]
    return subtotal


def net_with_surcharge(lines):
    amount = 0
    for line in lines:
        amount += line["unit_cost"] * line["units"]
    if amount >= 250:
        amount += 12
    return amount


def net_after_rebate(lines):
    amount = 0
    for line in lines:
        amount += line["unit_cost"] * line["units"]
    return amount * 0.95


def concise_amount(lines):
    return sum(line["unit_cost"] * line["units"] for line in lines)


def amount_with_default(lines):
    amount = 0
    for line in lines:
        amount += line.get("unit_cost", 0) * line["units"]
    return amount


def net_amount_rounded(lines):
    amount = 0
    for line in lines:
        amount += round(line["unit_cost"] * line["units"], 2)
    return amount
