def sum(a,b):
    return a+b

def test_calc_sum1():
    result = sum(2,3)
    assert result==5

def test_calc_sum2():
    result = sum(3,3)
    assert result==6

def test_calc_sum3():
    result = sum(5,5)
    assert result==10

def test_calc_sum4():
    result = sum(6,6)
    assert result==12

def test_calc_sum5():
    result = sum(7,7)
    assert result==14


