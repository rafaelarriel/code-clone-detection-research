"""Warehouse operations."""

def total_received(batches):
    count = 0
    for batch in batches:
        count += batch["pieces"]
    return count


def units_received(shipments):
    total = 0
    for shipment in shipments:
        total += shipment["pieces"]
    return total


def count_in_transit(records):
    qty = 0
    for record in records:
        qty += record["pieces"]
    return qty


def received_via_sum(batches):
    return sum(batch["pieces"] for batch in batches)


def received_nonnegative(batches):
    count = 0
    for batch in batches:
        count += max(batch["pieces"], 0)
    return count


def total_received_with_audit(batches):
    count = 0
    for batch in batches:
        count += batch["pieces"]
    if count < 0:
        raise ValueError("negative total")
    return count
