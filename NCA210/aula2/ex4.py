# Faça um programa que gera 100 vezes um número aleatório entre 1 e 100 e exiba qual foi o maior número gerado e quantas vezes o maior número foi atualizado.

from random import randrange

num_list = []

for i in range(1, 101):
    numero = randrange(1, 101)
    num_list.append(numero)

print(num_list)
print(f"O maior número é {max(num_list)} e aparece {num_list.count(max(num_list))} vez(es)")

