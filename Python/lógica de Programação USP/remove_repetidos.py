def main():
    lista = [2,4,2,2,3,3,1]
    print(remove_repetidos(lista))
    
    print(remove_repetidos([1, 2, 3, 3, 3, 4]))

    print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))

def remove_repetidos(n):
    lista = sorted(n)
    aux = []
    for i in lista:
        if not i in aux:
            aux.append(i)
    return aux


main()