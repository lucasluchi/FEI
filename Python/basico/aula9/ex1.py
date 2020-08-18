# Faça um programa que calcule o valor de um imposto de renda em um país fictício. 
# O usuário entrará com o valor do salário com duas casas decimais, seu programa deve calcular o valor que o usuário pagará de imposto seguindo as regras adiante.
# De 0 a 2000.00 o salário é isento de imposto, de 2000.01 a 3000.00 o imposto é de 8%, de 3000.01 a 4500.00 o imposto é de 18% e acima de 4500.00 o imposto é de 28%. 
# Lembre-se que cada porcentagem de imposto incide apenas naquela faixa de renda, caso o salário do usuário seja 3200.00 por exemplo, o imposto a ser pago pode ser 
# calculado por 8% de 1000 + 18% de 200.00.

salario = round(float(input("Entre com o valor do salário: ")), 2)
imposto_total = 0.00

if salario > 2000.00:
    if salario > 3000.00:
        imposto_total += (1000.00)  * 0.08
    else:
        imposto_total += (salario)  * 0.08

if salario > 3000.00:
    if salario > 4500.00:
        imposto_total += (1500.00)  * 0.18
    else:
        imposto_total += (salario - 3000.00)  * 0.18

if salario > 4500.00:
    imposto_total += (salario - 4500.00)  * 0.28


print(f"O total de imposto a pagar é: R$ {round(imposto_total,2):.2f}")
    