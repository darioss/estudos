def main():
    lista = [1, 5, 40, 9, 0, 42, -1]
    print(lista)
    print(inverte(lista))

def inverte(n):
    listaInverida = []
    contador = len(n)-1
    for i in range(len(n)-1, 0, -1):
        while contador >= 0:
            listaInverida.append(n[contador])
            contador -= 1
    return listaInverida

main()