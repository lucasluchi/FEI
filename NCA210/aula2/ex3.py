# Escreva um programa que leia números digitados pelo usuário. O programa deve ler os números até que 0 (zero) seja digitado.
# Quando 0 for digitado, o programa deve exibir a quantidade de dígitos que foram digitados, a somatória destes dígitos e a média aritmética.

quantidade = 0
soma = 0
num = int(input("Digite um número: "))

while(num != 0):
    quantidade += 1
    soma += num
    num = int(input("Digite um número: "))

print(f"Quantidade de Dígitos: {quantidade}")
print(f"Soma dos valores digitado: {soma}")
print(f"Média dos valores digitado: {round(soma/quantidade,2):.2f}")