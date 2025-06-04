"""
Crie uma função recursiva para calcular o n-ésimo termo da sequência de
Fibonacci.
"""
def fibonacci(n: int):
    if n < 0:
        raise ValueError("O valor de n deve ser maior ou igual a 0.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

resultado = fibonacci(6)
print(f"O 6º termo da sequência de Fibonacci é: {resultado}")


"""
Escreva uma função lambda que receba dois números e retorne o maior deles.
"""
maior = lambda x, y: x if x > y else y

resultado = maior(10, 25)
print(f"O maior número é: {resultado}")

"""
Implemente uma função que receba uma lista e uma função como parâmetros,
e aplique a função a cada elemento da lista.
"""
def aplicar_funcao(lista: list, funcao):
    return [funcao(elemento) for elemento in lista]

numeros = [1, 2, 3, 4, 5]
dobro = lambda x: x * 2
resultado = aplicar_funcao(numeros, dobro)
print(f"Lista com função aplicada (dobro): {resultado}")
