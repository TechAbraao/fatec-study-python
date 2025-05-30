from datetime import datetime

"""
Crie um programa que solicite o nome e a idade do usuário e imprima uma
mensagem personalizada.
"""
def nome_idade():
    try:
        nome: str = input("Digite seu nome: ")
        if not nome.isalpha():
            raise ValueError("O nome deve conter apenas letras.")
    except ValueError as e:
        print(f"Erro: {e}")
        exit()

    try:
        idade: int = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: Digite um número inteiro válido para a idade!")
        exit()

    print(f"Olá {nome}, sei que você tem {idade} anos de idade.")

# nome_idade()


"""
Escreva um programa que peça dois números e imprima a soma, subtração,
multiplicação e divisão entre eles.
"""
def operacoes_matematicas():
    try:
        numero_um = float(input("Digite o primeiro número: "))
        numero_dois = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Você deve digitar números válidos.")
        exit()

    print("\nResultados das operações:")
    print(f"Soma: {numero_um + numero_dois}")
    print(f"Subtração: {numero_um - numero_dois}")
    print(f"Multiplicação: {numero_um * numero_dois}")

    if numero_dois != 0:
        print(f"Divisão: {numero_um / numero_dois}")
    else:
        print("Divisão: Erro - divisão por zero não é permitida.")

# operacoes_matematicas()

"""
Escreva um programa que peça o ano de nascimento do usuário e calcule sua
idade.
"""
def idade_pelo_nascimento():
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento: "))
    except ValueError:
        print("Erro: digite um ano válido.")
        exit()

    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos de idade.")

# idade_pelo_nascimento()