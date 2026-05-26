def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    is_price_valid = price > 0
    is_discount_valid = 0 <= discount <= 100

    if not is_price_valid:
        return "The price should be greater than 0"
    if not is_discount_valid:
        return "The discount should be between 0 and 100"

    return round(price - (price * (discount/100)), 2)
print(apply_discount(100, 20))