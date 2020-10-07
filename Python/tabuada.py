def  main():

    linha = 1
    coluna = 1
    while linha <= 10:
        while coluna <= 10:            
            print(linha * coluna, end="\t")
            coluna += 1
        linha +=1
        print (" ")
        coluna = 1


    print("***********")
    tab = 1
    i = 1
    while tab <= 10 and i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
        tab = tab + 1
    print()
        



main()