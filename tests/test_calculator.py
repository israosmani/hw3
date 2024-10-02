from calculator import add, subtract
def test_addition():
    assert add(2,2) == 4
def test_subtraction():
    assert subtract(2,2) == 0
def test_multiply():
    assert Calculator.multiply(2,2) == 4
def test_divide():
    assert Calculator.divide(2,2) == 1