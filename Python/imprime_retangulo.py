def main():
    largura = int(input("Informe a largura do do retângulo: "))
    altura = int(input("Informe a altura do do retângulo: "))
    y = 0
    z = 0
    while y < altura:
        while z < largura:
            if z == largura - 1:
                print("#")
            else:
                print("#", end="")
            z += 1
        y += 1
        z = 0

main()