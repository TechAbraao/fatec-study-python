"""
Crie uma função que receba uma lista de números e retorne a soma de todos os
elementos.
"""
def somar_lista(numeros: list):
    soma = sum(numeros)
    return soma


lista_exemplo = [1, 2, 3, 4, 5]
resultado = somar_lista(lista_exemplo)
print(f"Soma dos elementos: {resultado}")


"""
Escreva um programa que remova todos os elementos duplicados de uma lista.
"""
def remover_duplicatas(lista: list):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
resultado = remover_duplicatas(lista_com_duplicatas)
print(f"Lista sem duplicatas: {resultado}")

"""
Implemente uma função que receba duas listas e retorne uma nova lista
contendo apenas os elementos comuns entre elas.
"""
def elementos_comuns(lista1: list, lista2: list):
    comuns = list(set(lista1) & set(lista2))
    return comuns

lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]
resultado = elementos_comuns(lista_a, lista_b)
print(f"Elementos comuns: {resultado}")
