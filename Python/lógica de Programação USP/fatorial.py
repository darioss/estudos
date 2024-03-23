def main():
    n = int(input("Digite o valor de n: "))
    i = 1
    fatorial = 1
    while n >= i:
        fatorial *= i
        i += 1
    print(fatorial)
main()