from math import ceil as math_ceil

def ceil(x, s):
    return s * math_ceil(x/s)

def apply_discount(price, discount):
    cost = price * discount
    if price < 20:
        result = price
    elif price >= 20 and price < 50:
        result = ceil(cost / 0.68, 10) - 0.01
    elif price >= 50 and price < 100:
        result = ceil(cost / 0.68, 5) - 0.01
        print(result)
    elif price >= 100:
        result = ceil(cost / 0.68, 10) - 0.01
    else: result = price
    return result

discount_codes = {
    "B": 0.6,
    "BY": 0.6 * 0.9,
    "BYY": 0.6 * 0.9 * 0.9,
    "B15": 0.6 * 0.85,
    "B20": 0.6 * 0.8,
    "B25": 0.6 * 0.75,
    "B25+5": 0.6 * 0.75 * 0.95,
    "A": 0.5,
    "AY": 0.5 * 0.9,
    "A20": 0.5 * 0.8,
}

def calculate_discount(retail, cost, default = "A"):
    for _, code in discount_codes.items():
        cost_calc = round(code * retail, 2)
        if cost_calc == round(cost, 2):
            return code
    return discount_codes[default]