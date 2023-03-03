from discounts import calculate_discount, discount_codes
import pytest

tests = [
    (401, 240.6, discount_codes['B']), # test B code
    (95, 51.30, discount_codes['BY']), # test BY code
    (77.25, 37.54, discount_codes['BYY']), # test BYY code
    (279, 142.29, discount_codes['B15']), #  test B15 code
    (279, 133.92, discount_codes['B20']), # test B20 code
    (119.25, 53.66, discount_codes['B25']), # test B25 code
    (409, 174.85, discount_codes['B25+5']), # test B25+5 code
    (881, 440.5, discount_codes['A']), # test A code
    (34.5, 15.53, discount_codes['AY']), # test AY code
    (119.25, 47.7, discount_codes['A20']), # test A20 code
    (75, 38.5, discount_codes['A']), # return A code as default if code not found
]

test_default = [
    (454.00, 227.00, "B", discount_codes['A']), # Changing default still determines correct code
    (75, 38.5, "BY", discount_codes['BY']), # Default argument works correctly if no discount found
]

# test without default argument
@pytest.mark.parametrize("list_price, dealer_cost, expected_output", tests)
def test_calculate_discount(list_price, dealer_cost, expected_output):
    assert calculate_discount(list_price, dealer_cost) == expected_output

# Test optional default parameter
@pytest.mark.parametrize("list_price, dealer_cost, default, expected_output", test_default)
def test_calculate_discount_default(list_price, dealer_cost, default, expected_output):
    assert calculate_discount(list_price, dealer_cost, default) == expected_output