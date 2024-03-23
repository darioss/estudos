def main():
    lista = [1,2,3,4,5,6,7,8,9]
    print(soma_elementos(lista))

def soma_elementos(n):
    soma = 0
    for i in n:
        soma += i
    return soma

main()