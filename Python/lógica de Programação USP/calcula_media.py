def main():
    entrada = float(input("Informe a nota: "))
    notas = []
    i = 0
    soma = 0
    media = 0

    while 0 <= entrada <= 10:
        notas.append(entrada)
        i += 1
        entrada = float(input("Informe a nota: "))

    z = len(notas) - 1    
    status = " "
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    destaques = 0

    while z >= 0:
        if notas[z] <= 3:
            reprovados +=1

        elif 3 < notas[z] < 7:
            recuperacao += 1
        
        else:
            aprovados += 1
            if notas[z] >= 9:    
                destaques += 1
        
        z -= 1

        print(notas)

        print("Total de alunos = " + str(len(notas)))
        print("Numero de alunos reprovados = " + str(reprovados))
        print("Numero de alunos de recuperacao = " + str(recuperacao))
        print("Numero de alunos aprovados = " + str(aprovados))
        print("Numero de alunos com desempenho muito bom = " + str(destaques))
    

main()    