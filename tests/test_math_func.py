from . import math_func

def test_add():
    assert math_func.add(10, 20) == 30 
    assert math_func.add(10) == 15
    
def test_product():
    assert math_func.product(10, 5) == 50
    assert math_func.product(5) == 25
    