'''
Exercício 9.3
Dados dois números naturais m e n e duas sequências ordenadas com m e n números inteiros,
obter uma única sequência ordenada contendo todos os elementos das sequências originais sem repetição.

Sugestão: Imagine uma situação real, por exemplo, dois fichários de uma biblioteca.

'''
def main():
    m = 10
    n = 35
    print(monta_listas(m, n))

def monta_listas(m,n):
    lista1 = []
    lista2 = []
    listaUnica = []
    aux = []

    for i in range(m+1):
        lista1.append(i)

    for i in range(n+1):
        lista2.append(i)

    aux = lista1 + lista2
    for i in aux:
        if i not in listaUnica:
            listaUnica.append(i)
    return listaUnica
main()