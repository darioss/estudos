def main():
    n = int(input("Digite um número inteiro positivo: "))
    print(verifica_quantidade_primos(n))

def verifica_quantidade_primos(n):
    x = n
    lenght = 0
    while x > 1:
        primos = n_primos(x)
        if primos == True:
            lenght += 1
        x -= 1
    return lenght
        
def n_primos(n):
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