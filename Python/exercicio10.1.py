from math import e
import random

def pertence(item,lista):
    '''(objeto, list) -> bool

    Recebe uma lista de itens e um item e
    retorna True se o item eh um elemento da lista e
    False em caso contrario.
    '''
    if item in lista:
        return True
    else:
        return False

def geraLista(tamanho, limiteAleatorio, ordem):
    '''
    Recebe o tamanho da lista, o limite aleatório para o qual serão
    gerados números para a lista e TRUE ou FALSE para a definir se
    a lista é ou não ordenada.

    Retorna uma lista com números aleatórios excluídos os registros
    repetidos, podendo ser ou não ordenada.

    Exemplo de uso:
    geraLista(12, 9, TRUE) - Gera uma lista ordenada com 12 números
    e com valores variando de 0 a 9 na geração aleatória.

    Sempre que tamanho for maior que limiteAleatorio a lista retornada
    será menor que o tamanho repassado como parâmetro, pois serão eliminados
    os valores duplicados

    '''
    lista = []
    aux = []
    for i in range(tamanho):
        lista.append(random.randint(0, limiteAleatorio)) 

    for i in lista:
        if not i in aux:
            aux.append(i)
   
    if ordem:
        return sorted(aux)
    else:
        return aux
#---------------------------------------------------
def indice(item, lista):
    '''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None
    '''
    print("Vixe! Ainda nao fiz a funcao!")

    if item in lista:
        return lista.index(item)
    else:
        return "item não pertence a lista"


# testes
lista  = [1, "oi", 3.14, 7, True]
print(geraLista(5, 8, False))

print(pertence("oi", lista))

print("O índice é", indice(3.14, lista))

# teste 1
if pertence("oi",lista):
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if pertence(True,lista):
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if not pertence(False,lista):
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

# outros testes
if pertence(False,lista):
    print("Passou no quarto teste! :-)")
else:
    print("Não passou no quarto teste! :-(")