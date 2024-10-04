from calculator import add, subtract

def test_addition():
    assert add(2,2) == 4

def test_subtraction():
    assert subtract(2,2) == 0