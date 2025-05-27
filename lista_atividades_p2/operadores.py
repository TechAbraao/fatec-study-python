"""
Escreva um programa que calcule e imprima a área e o perímetro de um
retângulo com base na largura e altura fornecidas.
"""

def calcular_retangulo(largura: float, altura: float):
    if largura == 0 or altura == 0:
        raise ValueError("A largura e a altura devem ser diferentes de zero.")

    area = largura * altura
    perimetro = 2 * (largura + altura)

    return area, perimetro

area, perimetro = calcular_retangulo(5, 3)
print(
    f"Área: {area} - Perímetro: {perimetro}"
)

"""
Crie um programa que calcule o IMC (Índice de Massa Corporal) usando a
fórmula: IMC= peso / (altura²).
"""
def calcula_IMC(peso: float, altura: float):
    if peso == 0 or altura == 0:
        raise ValueError("A altura e o peso devem ser diferentes de zero.")
    calculo = peso / (altura * altura)

    return calculo

"""
Escreva um programa que verifique se um número é par ou ímpar usando o
operador módulo (%).
"""
def par_ou_impar(numero: int):
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
