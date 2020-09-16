def main():
    # comandos
    quadrado = input("Digite o valor correspondente ao lado de um quadrado:")
    aux = int(quadrado)

    area = aux*aux
    perimetro = aux*4

    print("perímetro:", perimetro, "- área:", area)

#------
# a linha a seguir inicia a execução do programa
main()