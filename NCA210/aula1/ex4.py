vazao = int(input("Entre com a vazao: "))
capacidade = int(input("Entre com a capacidade: "))
total_segundos = (capacidade/vazao)
horas = total_segundos//3600.0
minutos = (total_segundos//60.0) - (horas*60)

print("%.1f horas" %(horas), "%.1f minutos" %(minutos), "%.1f segundos" %(total_segundos%60.0))