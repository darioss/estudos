def main():
    import math

    x1 = float(input("Informe o X do primeiro ponto: "))
    y1 = float(input("Informe o Y do primeiro ponto: "))
    x2 = float(input("Informe o X do segundo ponto: "))
    y2 = float(input("Informe o Y do segundo ponto: "))

    distancia = math.sqrt((x1-x2)**2 +(y1-y2)**2)
    
    if distancia >= 10:
        print("longe")
    else:
        print("perto")
main()