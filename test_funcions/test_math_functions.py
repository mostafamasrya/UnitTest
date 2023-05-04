import math_functions

def test_add():
    assert math_functions.add(7,3) == 10
    assert math_functions.add(7) == 9
    assert math_functions.add(5) == 7
    assert math_functions.add(-3,3) == 0

def test_product():
    assert math_functions.product(5,5) == 25
    assert math_functions.product(0,5) == 0
    assert math_functions.product(5) == 10