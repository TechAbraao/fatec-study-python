"""
Crie um programa que verifique se um número é positivo, negativo ou zero.
"""
def positivo_negativo_zero():
    try:
        numero = int(input("Digite um número e verifique seu sinal: "))

        if numero > 0:
            print("Número positivo.")
        elif numero < 0:
            print("Número negativo.")
        else:
            print("Número igual a zero.")

    except ValueError:
        print("Erro: digite um número válido.")
        exit()

positivo_negativo_zero()

"""
Escreva um programa que classifique um triângulo como equilátero, isósceles
ou escaleno com base nos valores dos lados.
"""
def classificar_triangulo():
    try:
        lado1 = float(input("Digite o valor do primeiro lado: "))
        lado2 = float(input("Digite o valor do segundo lado: "))
        lado3 = float(input("Digite o valor do terceiro lado: "))

        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            if lado1 == lado2 == lado3:
                print("Triângulo equilátero.")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Triângulo isósceles.")
            else:
                print("Triângulo escaleno.")
        else:
            print("Os valores informados não formam um triângulo válido.")

    except ValueError:
        print("Erro: digite apenas números válidos.")

classificar_triangulo()

"""
Crie um programa que simule um caixa eletrônico, verificando se o saldo é
suficiente para um saque.
"""
def simular_caixa_eletronico():
    try:
        saldo = float(input("Digite o saldo da conta: "))
        saque = float(input("Digite o valor que deseja sacar: "))

        if saque <= 0:
            print("Erro: o valor do saque deve ser maior que zero.")
        elif saque <= saldo:
            print(f"Saque de R${saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    except ValueError:
        print("Erro: digite apenas números válidos.")

simular_caixa_eletronico()
