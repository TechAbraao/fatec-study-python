
"""
Crie um programa que divida dois números fornecidos pelo usuário, tratando a
divisão por zero.
"""
def dividir_numeros():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))

        resultado = numerador / denominador
        print(f"O resultado da divisão é: {resultado}")

    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except ValueError:
        print("Erro: digite apenas números válidos.")

dividir_numeros()

"""
Escreva um programa que tente converter uma string para inteiro, tratando o
erro caso a string não seja um número.
"""
def converter_string_para_inteiro():
    try:
        texto = input("Digite um número (string): ")
        numero = int(texto)
        print(f"A conversão foi bem-sucedida! Número inteiro: {numero}")
    except ValueError:
        print("Erro: a string digitada não representa um número inteiro válido.")

converter_string_para_inteiro()

"""
Crie um programa que abra um arquivo para leitura e trate o erro caso o
arquivo não exista.
"""
def abrir_arquivo():
    try:
        nome_arquivo = input("Digite o nome do arquivo a ser aberto: ")
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: o arquivo especificado não foi encontrado.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

abrir_arquivo()

