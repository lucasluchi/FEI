# Faça um programa que recebe um número inteiro correspondente à idade de uma pessoa em dias e transforma esse valor em anos, meses e dias. 
# Para facilitar o cálculo, considere que o ano possui 365 dias e todos os meses apenas 30 dias.

idade = int(input("Entre com usa idade: "))

anos = idade//365
idade -= anos*365

meses = idade//30
idade -= meses*30

dias = idade

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)