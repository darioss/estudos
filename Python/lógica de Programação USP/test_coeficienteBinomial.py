def main():
    print(coeficienteBinomial(5,3))

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -=1
    return fat

def coeficienteBinomial(n,p):
    return fatorial(n) / (fatorial(p) * fatorial(n-p))

#teste a função fatorial
def test_fatorial1():
    assert fatorial(1) == 1
def test_fatorial2():
    assert fatorial(2) == 2
def test_fatorial0():
    assert fatorial(0) == 1
def test_fatorial5():
    assert fatorial(5) == 120

#Teste a função coeficiente
def test_coeficiente5():
    assert coeficienteBinomial(5,5) == 1
def test_coeficiente0():    
    assert coeficienteBinomial(5,0) == 1
def test_coeficiente1():    
    assert coeficienteBinomial(5,1) == 5

main()