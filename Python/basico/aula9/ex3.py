# Faça um programa que leia três valores inseridos pelo usuário e calcula as raízes da equação de Bhaskara. 
# Caso não seja possível calcular as raízes, imprima uma mensagem ao usuário, informando-o que não é possível executar o cálculo. 
# Considere que o usuário irá inserir os valores na seguinte ordem: a, b e c (ax² + bx + c).
import math

print("Entre com os valores de a, b e c para o cálculo das raízes equação de Bhaskara\n")

a = round(float(input("Entre com o valor de a: ")),1)
b = round(float(input("Entre com o valor de b: ")),1)
c = round(float(input("Entre com o valor de c: ")),1)

if a == 0:
    print("Impossível calcular")
else:
    print(f"Equação: {a}x² + {b}x + {c}\n")

    r1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)5
    r2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    print(f"R1 = {r1}")
    print(f"R2 = {r2}")