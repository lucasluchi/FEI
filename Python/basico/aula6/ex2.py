# Faça um programa que recebe um número inteiro correspondente a duração de um evento esportivo em segundos
# transforme esse tempo para o formato horas:minutos:segundos e imprima na tela.

duracao = int(input("Entre com o tempo de duração em segundos: "))

horas = duracao//3600
duracao -= horas*3600

minutos = duracao//60
duracao -= minutos*60

segundos = duracao

print("A duração do evento foi de {}:{}:{}".format(horas,minutos,segundos))