def calculate(a,b):
    return a*b

def test_calculate():
    assert calculate(5,5) == 25
    assert calculate(2,5) == 10
    assert calculate(5,2) == 10