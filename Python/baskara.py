import math

def main():
    raizes()    

def nums():
    i = 0
    entrada = 0
    x = []
    while i < 3:
        entrada = input("informe os números: ")
        x.append(entrada)
        i += 1
    return x
             
def delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def calcRaiz():
    x = nums()
    d = delta(int(x[0]), int(x[1]), int(x[2]))
    raizes = []
    if d >= 0:
        x1 = (-int(x[1]) + math.sqrt(d)) / (2*int(x[0]))
        x2 = (-int(x[1]) - math.sqrt(d)) / (2*int(x[0]))
        raizes.append(str(x1))
        raizes.append(str(x2))
    else:
        raizes = []
    return raizes

def reverse(a, b):     
    aux = b
    b = a
    a = aux

def raizes():
    r = calcRaiz()
    if len(r) > 0:
        x1 = r[0]
        x2 = r[1]
        if x1 != x2:
            reverse(x1, x2)   
            print("as raízes da equação são", x1, "e", x2)
        elif x1 == x2:
            print("a raiz desta equação é",  x1)      
    else:    
        print("esta equação não possui raízes reais")
    
main()    