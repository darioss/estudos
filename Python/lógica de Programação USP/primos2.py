def main():
    n = 1
    if n >= 0:
        while n >= 0:
            n = int(input("Informe um número inteiro positivo: "))
            if n >= 0:
                if ePrimo(n):
                    print(n, "é primo")
                else:
                    print(n, "não é primo")
            else:
                print("O número informado encerrou o programa.")

def ePrimo(n):
    fator = 2
    if n == 2 or n == 3:
        return True
    else:
        while n % fator != 0 and fator <= n/2:
            fator += 1
            if n % fator == 0:
                return False
            else:
                return True

main()