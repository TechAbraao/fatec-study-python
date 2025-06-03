"""
Escreva um programa que gere os N primeiros termos da sequência de Fibonacci utilizando uma lista para armazená-los. N é um número inteiro a ser lido do teclado e deve, obrigatoriamente, ser maior ou igual a 2. E mostre a lista com a sequência de Fibonacci.
"""

n = int(input("Digite o número de termos da sequência de Fibonacci (mínimo 2): "))

while n < 2:
    n = int(input("Número inválido. Digite um número maior ou igual a 2: "))

fibonacci = []
a, b = 0, 1

for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("Sequência de Fibonacci:", fibonacci)