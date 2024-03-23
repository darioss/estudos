def main():
    n = input("Digite um número inteiro: ")
    aux = int(n)
    i = 0
    soma = 0

    while i < len(n):
        soma += int(n[i])
        i += 1
    print(soma)    
main()