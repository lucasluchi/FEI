# Faça um programa que calcule o salário de um funcionário. Seu programa deve receber do usuário 
# a quantidade de horas trabalhadas e o valor que recebe por hora, calcule o salário e imprima-o na tela.

horas_trabalhadas = int(input("Entre com a quantidade de horas trabalhadas: "))
valor_hora = float(input("Entre com o valor da sua hora: "))

print("Seu salário é de R$ %.2f" % (horas_trabalhadas * valor_hora))