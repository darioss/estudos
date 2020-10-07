def main():
    lista = [10, 13, 16, 10, 9, 6, 12, 6, 7]
    print(lista)
    print(remove_repetidos(lista))

def remove_repetidos(n):
    aux = []
    for i in n:
        if i not in aux:
            aux.append(i)
    return aux

main()