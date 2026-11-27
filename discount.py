def apply_coupon(subtotal: float, percent: float) -> float:
    return round(subtotal - (subtotal * percent / 100), 2)
