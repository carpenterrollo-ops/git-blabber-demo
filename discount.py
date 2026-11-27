def apply_coupon(subtotal: float, percent: float) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal must be non-negative.")
    if not 0 <= percent <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    return round(max(0.0, subtotal - (subtotal * percent / 100)), 2)
