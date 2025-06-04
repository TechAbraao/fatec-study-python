"""
Crie uma função que receba uma lista de tuplas contendo nome e idade de
pessoas, e retorne a pessoa mais velha.
"""


def pessoa_mais_velha(pessoas: list):
    if not pessoas:
        raise ValueError("A lista não pode estar vazia.")

    mais_velha = max(pessoas, key=lambda pessoa: pessoa[1])
    return mais_velha


lista_pessoas = [("Ana", 25), ("Carlos", 42), ("Beatriz", 36)]
resultado = pessoa_mais_velha(lista_pessoas)
print(f"Pessoa mais velha: {resultado[0]} com {resultado[1]} anos.")


"""
Escreva um programa que converta uma lista de coordenadas (x, y) em uma
tupla contendo as médias de x e y.
"""


def media_coordenadas(coordenadas: list):
    if not coordenadas:
        raise ValueError("A lista de coordenadas não pode estar vazia.")

    soma_x = sum(x for x, y in coordenadas)
    soma_y = sum(y for x, y in coordenadas)
    total = len(coordenadas)

    media = (soma_x / total, soma_y / total)
    return media

coordenadas_exemplo = [(2, 4), (6, 8), (4, 2)]
resultado = media_coordenadas(coordenadas_exemplo)
print(f"Média das coordenadas: {resultado}")

"""
Implemente uma função que receba uma tupla de strings e retorne uma nova
tupla com o comprimento de cada string.
"""
def comprimento_strings(tuplas_de_texto: tuple):
    comprimentos = tuple(len(string) for string in tuplas_de_texto)
    return comprimentos

tupla_exemplo = ("python", "chatgpt", "IA", "OpenAI")
resultado = comprimento_strings(tupla_exemplo)
print(f"Comprimento das strings: {resultado}")

