def main():
    largura = int(input("Informe a largura do do retângulo: "))
    altura = int(input("Informe a altura do do retângulo: "))
    y = 0
    z = 0
    while y < altura:
        if y == 0 or y == altura - 1:
            while z < largura:
                if z == largura - 1:
                    print("#")
                else:
                    print("#", end="")
                z += 1
            y += 1
            z = 0
        else:
            while z < largura:
                if z == 0:
                    print("#", end="")
                elif  z == largura - 1:
                    print("#")
                else:
                    print(" ", end="")
                z += 1
            y += 1
            z = 0

main()