"""
Converta uma string contendo um número para inteiro e realize uma operação
matemática com ele.
"""
numero_str = "10"
numero_int = int(numero_str)
resultado = numero_int + 5

print(f"String: {numero_str}")
print(f"Convertido para inteiro: {numero_int}")
print(f"Soma com 5: {resultado}")


"""
Crie um programa que converta um valor em ponto flutuante para inteiro e
mostre a diferença entre os dois.
"""
valor_float = 7.9
valor_inteiro = int(valor_float)
diferenca = valor_float - valor_inteiro

print(f"Valor float: {valor_float}")
print(f"Convertido para inteiro: {valor_inteiro}")
print(f"Perda de precisão: {diferenca}")


"""
Converta uma lista de strings numéricas para uma lista de inteiros.
"""
lista_str = ["1", "2", "3", "4", "5"]
lista_int = [int(valor) for valor in lista_str]

print(f"Lista original (strings): {lista_str}")
print(f"Lista convertida (inteiros): {lista_int}")