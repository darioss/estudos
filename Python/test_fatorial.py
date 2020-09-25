def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -=1
    return fat

#teste a função fatorial
def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial2():
    assert fatorial(2) == 2

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial5():
    assert fatorial(5) == 120
