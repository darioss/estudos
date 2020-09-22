def main():
    n = int(input("Digite um número inteiro: "))
    primo = False

    if n % 2 == 0:
        if not n != 2:
            primo = True
    elif n == 1:
        primo = False
    elif n % 3 == 0:
        if not n != 3:
            primo = True
    elif n % 5 == 0:
        if not n != 5:
            primo = True
    elif n % 7 == 0:
        if not n != 7:
            primo = True
    else:
        primo = True  

    if primo:
        print("primo")
    else:
        print("não primo")          
main()