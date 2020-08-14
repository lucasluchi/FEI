# Faça um programa que calcule a média ponderada de um aluno. Leia três notas, a primeira nota tem peso 2, 
# a segunda nota tem peso 3 e a terceira nota tem peso 5. Calcule a média ponderada e imprima o resultado na tela. 
# Considere que cada nota pode ir de 0 a 10.0.

print("Entre com os valores das 3 notas (valores de 0 a 10.0)")

nota1 = float(input("P1: "))
nota2 = float(input("P2: "))
nota3 = float(input("P3: "))

print("A média é de %.1f" % ((nota1*2 + nota2*3 + nota3*5)/10))