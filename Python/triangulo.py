def main():
    num = int(input("Digite um numero inteiro n (n<0): "))
    
    if num % 2 == 0:
        z = 1
        x = 0
        triangulo = []
        divisores = []
        
        #Monta a lista de divisores do número informado
        while z <= num:
            if num % z == 0:
                divisores.append(z)
            z += 1

        #Monta o trinângulo
        while len(divisores) >= x:
            if x < len(divisores) - 2:
                if (divisores[x + 1] == divisores[x] + 1) and (divisores[x + 2] == divisores[x] + 2) and (divisores[x] * divisores[x + 1] * divisores[x + 2] == num):
                    triangulo.append(divisores[x])
                    triangulo.append(divisores[x + 1])
                    triangulo.append(divisores[x + 2])
            x += 1

        print("Triângulo", triangulo)
        print("Divisores",divisores)
        print("Um numero triangular é composto pelo produto de 3 numeros consecutivos.")
        print("O numero", num, "e um triangulo formado pelo produto de", triangulo[0],",", triangulo[1],"e", triangulo[2])

    else:
        print("Este numero não é um triângulo")
main()