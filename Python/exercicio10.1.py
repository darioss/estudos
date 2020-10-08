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
    parametro = str(item)
    aux = []
    for i in range(len(lista)):
        aux.append(str(lista[i]))

    if parametro in aux:
        return aux.index(parametro)
    else:
        return "item não pertence à lista"

def contaOcorrencias(item, lista):
    '''
    Recebe um item e uma lista e conta quantas vezes o item
    aparece na lista.
    '''
    if item in lista:
        return lista.count(item)
    else:
        return "item não petence à lista"

def soma_elementos(inicio, fim, lista):
    '''
    Recebe uma lista e dois parametros de início e fim
    para a montagem de uma sub-lista a partir da lista
    original. Retorna a soma dos valores de cada indice
    da sub-lista.
    '''
    sublista = lista[inicio:fim]
    return sum(sublista)

# testes
lista  = [1, "oi", 3.14, 7, True, "oi", "oi"]
lista2  = [1, 2, 3, 4, 5]

print("######################################################")
print("######  -  TESTA A FUNÇÃO CONTA OCORRÊNCIAS  -  ######")
print("######################################################")
# teste 1
if contaOcorrencias("oi", lista) == 3:
    print("Passou no primeiro teste :-)")
else:
    print("Nao passou no primeiro teste! :-(")

if contaOcorrencias(True, lista):
    print("Passou no Segundo teste :-)")
else:
    print("Nao passou no segundo teste! :-(")

print("###########################################")
print("######  -  TESTA A FUNÇÃO ÍNDICE  -  ######")
print("###########################################")
# teste 1
if indice(3.14, lista) == 2:
    print("Passou no primeiro teste :-)")
else:
    print("Nao passou no primeiro teste! :-(")


if indice(7, lista) == 3:
    print("Passou no segundo teste :-)")
else:
    print("Nao passou no segundo teste! :-(")

if indice(True, lista) == 4:
    print("Passou no terceiro teste :-)")
else:
    print("Nao passou no terceiro teste! :-(")

if indice(718, lista) == 12:
    print("Passou no Quarto teste :-)")
else:
    print("Nao passou no quarto teste! :-(")


print("###############################################")
print("######  -  TESTA A FUNÇÃO GERA LISTA  -  ######")
print("###############################################")
# teste 1
if geraLista(5, 8, False):
    print("Gerou lista aleatória não ordenada :-)")
    print(geraLista(5, 8, False))
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if geraLista(5, 8, True):
    print("Gerou lista aleatória ordenada :-)")
    print(geraLista(5, 8, True))
else:
    print("Nao passou no primeiro teste! :-(")

print("#############################################")
print("######  -  TESTA A FUNÇÃO PERTENCE  -  ######")
print("#############################################")
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

print("#############################################")
print("####  - TESTA A FUNÇÃO SOMA ELEMENTOS -  ####")
print("#############################################")
# teste 1
if soma_elementos(0,len(lista2),lista2) == 15:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if soma_elementos(1,4,lista2) == 9:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if soma_elementos(2,2,lista2) == 0:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")
