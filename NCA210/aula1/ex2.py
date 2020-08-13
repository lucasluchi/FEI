valor_hora = int(input("Ganho por hora: "))
total_horas = int(input("Horas trabalhadas no mês: "))
salario_bruto = (total_horas*valor_hora)
ir = 0.11
inss = 0.08
sind = 0.05
liq = (1 - ir - inss - sind)

print("+Salário bruto %.2f" %salario_bruto)
print("-IR %.2f" %(salario_bruto * ir))
print("-INSS %.2f" %(salario_bruto * inss))
print("-Sindicato %.2f" %(salario_bruto * sind))
print("= Salário líquido %.2f" %(salario_bruto * liq))