'''
Exercício 9.4
Dados um número inteiro n e uma sequência com n números reais,
determinar a maior soma de um segmento da sequência (com pelo 
menos um elemento). Um segmento é uma subsequência de números consecutivos.

Para n == 12 e a sequência

5   -2   -2   -7   3   14  10  -3   9   -6   4   1
a soma do segmento de soma máxima é 3+14+10-3+9 = 33.
'''
def main():
    #lista = [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
    lista = [5, -28, -2, -70, 3, 89, 10, -3, 91, -6, 40, 1]
    print("O maior seguimento é de", soma_segmento(lista))
    
def soma_segmento(n):
    maiorSegmento = []
    segmento = 0
    
    for i in range(len(n)-4):
        segmento = n[i] + n[i + 1] + n[i + 2] + n[i + 3] + n[i + 4]
        maiorSegmento.append(segmento)
        segmento = 0
    
    return max(maiorSegmento)
       
main()