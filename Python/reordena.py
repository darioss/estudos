def main():
    lista = solicita_numero()
    trata_lista(lista)

def solicita_numero():
    n = -1
    lista = []
    while n != 0:
        n = int(input("Digite um número: "))
        if n > 0:
            lista.append(n)
    return lista

def trata_lista(n):
    contador = len(n) - 1
    if contador == 0:
        print(n[contador])
    else:
        for i in range(len(n)-1, 0, -1):
            while contador >= 0:
                print(n[contador])
                contador -= 1

main()