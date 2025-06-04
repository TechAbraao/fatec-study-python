"""
Crie um programa que conte quantas vezes uma determinada letra aparece em
uma string.
"""


def contar_letra(texto: str, letra: str):
    if len(letra) != 1:
        raise ValueError("A letra deve conter apenas um caractere.")

    quantidade = texto.count(letra)
    return quantidade


texto_exemplo = "programação em python"
letra_exemplo = "o"
quantidade = contar_letra(texto_exemplo, letra_exemplo)
print(f"A letra '{letra_exemplo}' aparece {quantidade} vezes no texto.")

"""
Escreva um programa que verifique se uma palavra é um palíndromo (lê-se
igual de trás para frente).
"""
def verificar_palindromo(palavra: str):
    palavra_limpa = palavra.replace(" ", "").lower()
    if palavra_limpa == palavra_limpa[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")


verificar_palindromo("radar")
verificar_palindromo("Python")

"""
Crie um programa que substitua todas as ocorrências de uma letra por outra
em uma string.
"""


def substituir_letra(texto: str, letra_antiga: str, letra_nova: str):
    if len(letra_antiga) != 1 or len(letra_nova) != 1:
        raise ValueError("As letras devem conter apenas um caractere.")

    novo_texto = texto.replace(letra_antiga, letra_nova)
    return novo_texto


texto_original = "banana"
resultado = substituir_letra(texto_original, "a", "e")
print(f"Texto modificado: {resultado}")
