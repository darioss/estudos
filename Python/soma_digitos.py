def main():
    numero = input("Digite um número: ")
    entrada = numero
    i = len(numero)
    soma = 0
    while i > 0:
        x = int(numero)%10
        #numero = int(numero)//10
        soma += x
        i -= 1 
    print("A soma dos dígitos do número", entrada, "é", soma)
main()    