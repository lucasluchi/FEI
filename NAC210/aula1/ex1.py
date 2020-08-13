km_rodados = int(input("Digite os km:"))
dias_alugados = int(input("Digite os dias:"))

print("R$ %.2f" % (km_rodados*0.15 + dias_alugados*60.0))