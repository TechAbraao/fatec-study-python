"""
Crie uma função que use range() para gerar uma lista de números pares entre 0
e n.
"""


def gerar_pares(n: int):
    if n < 0:
        raise ValueError("O valor de n deve ser maior ou igual a 0.")

    pares = list(range(0, n + 1, 2))
    return pares


resultado = gerar_pares(10)
print(f"Números pares entre 0 e 10: {resultado}")

"""
Escreva um programa que use range() para calcular a soma dos primeiros n
números naturais.
"""

def soma_naturais(n: int):
    if n < 0:
        raise ValueError("O valor de n deve ser maior ou igual a 0.")

    soma = sum(range(n + 1))
    return soma

resultado = soma_naturais(10)
print(f"Soma dos primeiros 10 números naturais: {resultado}")

"""
Implemente uma função que use range() para criar uma lista de potências de 2
até um determinado expoente.
"""


def potencias_de_dois(expoente_max: int):
    if expoente_max < 0:
        raise ValueError("O expoente deve ser maior ou igual a 0.")

    potencias = [2 ** i for i in range(expoente_max + 1)]
    return potencias

resultado = potencias_de_dois(5)
print(f"Potências de 2 até o expoente 5: {resultado}")
