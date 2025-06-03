"""
Escreva um programa que permaneça em laço lendo números inteiros enquanto os valores digitados forem diferentes de zero. Para cada valor digitado, adicione-o a uma lista na posição imediatamente anterior ao primeiro elemento da lista que seja maior ou igual a ele. Exiba a lista no final.
"""

lista = []

def inserir_ordenado(valor):
    for i, elemento in enumerate(lista):
        if valor <= elemento:
            lista.insert(i, valor)
            return
    lista.append(valor)

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    inserir_ordenado(numero)

print("Lista final:", lista)
