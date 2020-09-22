def main():    
    entrada = int(input("Digite um número inteiro: "))
    numero = str(entrada)
    anterior = 0
    atual = 0
    adj = False
    i = 0
    posic_anterior = 0
    posic_atual = 0
    
    while i < len(numero) and adj == False:
        if anterior == numero[i]:
           #variável de passagem
           adj = True
           atual = numero[i]
           posic_atual = i+1
    
        anterior = numero[i]
        posic_anterior = i
        i += 1

    if adj:
        print("sim")
        #print("A sequência " + numero + " possui o " + str(posic_anterior) + "º e o " + str(posic_atual) + "º dígitos adjascentes e iguais: " + anterior +  " e " + atual + "!!")
    else:
        print("não")
        #print("A sequência" + numero + "não apresenta dígitos adjascentes!!")    
main()