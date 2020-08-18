# Faça um programa que calcule quantos litros de combustível serão gastos em uma viagem ao utilizar um automóvel 
# que gasta 1 litro de combustível para percorrer 12 quilômetros. O usuário informará ao seu programa o tempo gasto 
# na viagem (em horas) na primeira linha e na segunda a velocidade média durante o trajeto (em km/h). 
# Imprima a quantidade necessária de combustível para realizar a viagem com três dígitos após o ponto.

horas = int(input("Entre com a quantidade de horas da viagem: "))
vel_media = int(input("Entre com a velocidade média da viagem: "))

trajeto_total = vel_media*horas
litros_total = trajeto_total/12

print(f"A quantidade de combustível necessária é de {litros_total:.3f} litros")