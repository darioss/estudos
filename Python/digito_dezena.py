numero = input("Digite um número inteiro: ")
tamanhoNumero = len(numero)
numeroDezenaAux = tamanhoNumero - 2

if tamanhoNumero < 2:
    numeroDezena = 0
else:
    numeroDezena = numero[numeroDezenaAux]

print("O dígito das dezenas é", numeroDezena)