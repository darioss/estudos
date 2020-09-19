def main():
    entrada = int(input("Digite um número inteiro: "))
    nums = []
    while entrada != 0:
        nums.append(entrada)
        entrada = int(input("Digite um número inteiro: "))
    i = 0
    par = 0
    impar = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            par += 1
        else:    
            impar += 1
        i += 1
    print("Os números inseridos foram", nums)    
    print("Existem %d numeros pares e %d numeros impares" %(par, impar)) 
main()