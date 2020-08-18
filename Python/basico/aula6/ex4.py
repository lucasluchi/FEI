# Faça um programa que calcule o menor número possível de notas (cédulas) que um valor, inserido pelo usuário, pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.

valor = int(input("Entre com o valor: "))

msg = (
    f"{valor//100} nota(s) de R$ 100,00 \n"
    f"{((valor%100)//50)} nota(s) de R$ 50,00 \n"
    f"{((valor%100)%50)//20} nota(s) de R$ 20,00 \n"
    f"{(((valor%100)%50)%20)//10} nota(s) de R$ 10,00 \n"
    f"{((((valor%100)%50)%20)%10)//5} nota(s) de R$ 5,00 \n"
    f"{(((((valor%100)%50)%20)%10)%5)//2} nota(s) de R$ 2,00 \n"
    f"{((((((valor%100)%50)%20)%10)%5)%2)//1} nota(s) de R$ 1,00 \n"
)

print(msg)