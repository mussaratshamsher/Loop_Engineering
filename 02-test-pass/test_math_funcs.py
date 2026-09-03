import math_funcs

def test_add():
    assert math_funcs.add(2, 3) == 5
    assert math_funcs.add(-1, 1) == 0

def test_subtract():
    assert math_funcs.subtract(5, 3) == 2
    assert math_funcs.subtract(10, 20) == -10

def test_multiply():
    assert math_funcs.multiply(3, 4) == 12
    assert math_funcs.multiply(-2, 5) == -10
