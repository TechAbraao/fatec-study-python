valor = input("Escreva qualquer coisa e descubra se tem um inteiro: ")

for caractere in valor:
    if caractere.isdigit():
        print("Tem um inteiro!")
        break
else:
    raise Exception("Nenhum número inteiro encontrado na string.")