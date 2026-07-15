from addition import add,subtract,multiply,divide

def test_add_positive():
    assert add(2,3)==5

def test_add_negative():
    assert add(-2,-3)==-5

def test_add_zero():
    assert add(0,0)==0

def test_add_pos_neg():
    assert add(5,-3)==2

def test_add_floats():
    assert add(2.5,3.1)==5.6

def test_subtract_positive():
    assert subtract(5,3)==2

def test_subtract_negative():
    assert subtract(-5,-3)==-2
def test_multiply_positive():
    assert multiply(2,3)==6
def test_multiply_negative():
    assert multiply(-2,-3)==6
def test_multiply_zero():
    assert multiply(0,0)==0

##testcase for division
def test_divide():
    assert divide(6,3)==2

def test_divide_by_zero():
    try:
        divide(5,0)
    except ZeroDivisionError:
        pass    
    else:
        assert False, "Expected ZeroDivisionError"