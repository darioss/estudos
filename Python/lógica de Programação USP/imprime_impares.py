def main():
    n = int(input("Digite o valor de n: "))
    i = 1
    z = 0

    while n >= i:
        while z <= 2 * n: 
            if  not z % 2 == 0: 
                print(z)
            z += 1
        i += 1
main()    