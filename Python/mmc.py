def main():
    n = int(input("Digite um número: "))
    
    fator = 2
    multiplicidade = 0

    while n > 1:
        while n % fator == 0:
            multiplicidade += 1
            n = n / fator
        if multiplicidade > 0:
            print("Fator " + str(fator) + " multiplicidade = " + str(multiplicidade) + " ---->" + str(fator) + "**" + str(multiplicidade))
        fator += 1
        multiplicidade = 0

main()