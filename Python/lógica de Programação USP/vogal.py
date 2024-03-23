def vogal(k):
    if k == "a" or k == "e" or k == "i" or k == "o" or k == "u":
        vogal = True
    elif k == "A" or k == "E" or k == "I" or k == "O" or k == "U":
        vogal = True
    else:
        vogal = False

    return(vogal)
    
vogal("A")