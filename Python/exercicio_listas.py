def main():
    numeros = pega_numeros()
    lista_invertida = inverte_lista(numeros)
    print("Lista de números:", numeros)
    print("Lista invertida", lista_invertida)


def pega_numeros():
    n = 1
    numeros = []
    while n > 0:
        n = int(input("Digite um número inteiro: "))
        numeros.append(n)
    return numeros

def inverte_lista(n):
    inverte = []
    i = len(n)
    while i > 0:
        inverte.append(n[i-1])
        i -= 1
    return inverte
    
main()