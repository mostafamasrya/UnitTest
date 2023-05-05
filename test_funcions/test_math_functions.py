import math_functions
import pytest
import sys
@pytest.mark.skipif(sys.version_info < (3,3),reason="skipped")
def test_add():
    assert math_functions.add(7,3) == 10
    assert math_functions.add(7) == 9
    assert math_functions.add(5) == 7
    assert math_functions.add(-3,3) == 0
    print("======-================asd==================----asd------")

def test_product():
    assert math_functions.product(5,5) == 25
    assert math_functions.product(0,5) == 0
    assert math_functions.product(5) == 10


def test_add_string():
    result = math_functions.add("hello ","world")
    assert result == "hello world"
    assert type(result) is str
    assert "asd" not in result


def test_product_string():
    result = math_functions.product("hello")
    result2 = math_functions.product("hello " ,3)
    assert result == "hellohello"
    assert result2 == "hello hello hello "