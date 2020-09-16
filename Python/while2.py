# escreva o seu programa
def main():
    num = int(input("Informe o numero inteiro que gostaria de saber o fatorial: "))
    
    #----CALCULANDO DE FORMA DESCRESCENTE----#
    i = num;
    fatorial = num;
    while i > 1:
        fatorial = fatorial*(i-1)
        i = i - 1 
    print("O valor de %d! eh igual a %d" %(num, fatorial))    
    
    #----CALCULANDO DE FORMA CRESCENTE----#
    i=2;# Começa no 2 por ser calculo fatorial que não inlcui o zero e o 1 pode ser desconsiderado por não modificar o resultado.
    fatorial = 1
    while i <= num:
        fatorial = fatorial*i
        i = i+1
    print("O valor de %d! eh igual a %d" %(num, fatorial))    
main()    