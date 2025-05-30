"""
Crie um programa que imprima os números de 1 a 20, pulando os múltiplos de
3.
"""
def imprimir_sem_multiplos_de_tres():
    try:
        for numero in range(1, 21):
            if numero % 3 != 0:
                print(numero)
    except Exception as e:
        print(f"Erro inesperado: {e}")

imprimir_sem_multiplos_de_tres()


"""
Escreva um programa que calcule a soma dos números de 1 a N, onde N é
informado pelo usuário.
"""
def somar_ate_n():
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n < 1:
            print("Erro: digite um número maior que zero.")
            return

        soma = 0
        for i in range(1, n + 1):
            soma += i

        print(f"A soma dos números de 1 até {n} é {soma}.")
    except ValueError:
        print("Erro: digite um número inteiro válido.")

somar_ate_n()

"""
Crie um programa que imprima a tabuada de um número informado pelo
usuário.
"""
def imprimir_tabuada():
    try:
        numero = int(input("Digite um número inteiro para ver sua tabuada: "))
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Erro: digite um número inteiro válido.")

imprimir_tabuada()
