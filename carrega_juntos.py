entrada = input("Digite os números separados por espaço: ")

try:
    numeros = [int(num) for num in entrada.split()]
except ValueError:
    raise Exception("Digite apenas inteiros!")

lista_letras = ["A", "B", "C"]

for numero, letra in zip(numeros, lista_letras):
    print(f"{letra}: {numero}")