primo = []
def maior_primo(n):
    entrada = n
    ePrimo(n)
    if entrada in primo:
        return(entrada)
    else:
        return(primo[0])
            
def ePrimo(n):
    while n >= 2:
        if n % 2 == 0:
            if not n != 2:
                primo.append(n)
        elif n % 3 == 0:
            if not n != 3:
                primo.append(n)
        elif n % 5 == 0:
            if not n != 5:
                primo.append(n)
        elif n % 7 == 0:
            if not n != 7:
                primo.append(n)
        elif n % 31 == 0:
            if not n != 31:
                primo.append(n)
        else:
            primo.append(n)
        n -= 1