
"""
Crie um programa que conte quantas vezes uma determinada letra aparece em
uma string.
"""
def contar_letra_em_string():
    try:
        texto = input("Digite uma frase ou palavra: ")
        letra = input("Digite a letra que deseja contar: ")

        if len(letra) != 1:
            print("Erro: digite apenas uma única letra.")
            return

        contagem = texto.count(letra)
        print(f"A letra '{letra}' aparece {contagem} vezes na string.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

contar_letra_em_string()

"""
Escreva um programa que verifique se uma palavra é um palíndromo (lê-se
igual de trás para frente).
"""
def verificar_palindromo():
    try:
        palavra = input("Digite uma palavra: ")
        palavra_formatada = palavra.lower().replace(" ", "")

        if palavra_formatada == palavra_formatada[::-1]:
            print(f"'{palavra}' é um palíndromo.")
        else:
            print(f"'{palavra}' não é um palíndromo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

verificar_palindromo()

"""
Crie um programa que substitua todas as ocorrências de uma letra por outra
em uma string.
"""
def substituir_letras():
    try:
        texto = input("Digite uma frase ou palavra: ")
        letra_antiga = input("Digite a letra que deseja substituir: ")
        letra_nova = input("Digite a nova letra: ")

        if len(letra_antiga) != 1 or len(letra_nova) != 1:
            print("Erro: digite apenas uma letra por campo.")
            return

        texto_substituido = texto.replace(letra_antiga, letra_nova)
        print(f"Texto após substituição: {texto_substituido}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

substituir_letras()

