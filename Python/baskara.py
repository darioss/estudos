def main():
    import math
    a = float(input("Qual o valor de a: "))
    b = float(input("Qual o valor de b: "))
    c = float(input("Qual o valor de c: "))

    delta = b ** 2 - 4 * a * c

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        if delta == 0:
            print("a raiz desta equação é",  x1)  
        else:
            if x1 > x2:
                aux = x2
                x2 = x1
                x1 = aux   
            print("as raízes da equação são", x1, "e", x2)
    else:
        print("esta equação não possui raízes reais")
    
main()    