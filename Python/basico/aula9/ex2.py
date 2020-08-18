# Faça um programa que identifique o local no plano (eixo cartesiano com duas dimensões) em que se encontra um ponto inserido pelo usuário 
# (primeira linha corresponde ao valor de x no par ordenado, a segunda linha corresponde ao valor de y). 
# Caso o ponto esteja na origem, imprima na tela a mensagem 'O ponto se encontra na origem'
# se o ponto estiver sobre um dos eixos imprima a mensagem 'O ponto se encontra sobre o eixo X', ou 'O ponto se encontra sobre o eixo Y' 
# dependendo da situação, caso nenhuma das situações descritas anteriormente descreva a posição do ponto, informe o quadrante em que ele se encontra.

x = round(float(input("Entre com o eixo x: ")),1)
y = round(float(input("Entre com o eixo y: ")),1)

if x == 0.0 and y == 0.0:
    print("O ponto se encontra na origem")
elif x == 0.0 and y != 0.0:
    print("O ponto se encontra sobre o eixo X")
elif x != 0 and y == 0.0:
    print("O ponto se encontra sobre o eixo Y")
elif x > 0.0 and y > 0.0:
    print("O ponto se encontra no 1° quadrante")
elif x < 0.0 and y > 0.0:
    print("O ponto se encontra no 2° quadrante")
elif x < 0.0 and y < 0.0:
    print("O ponto se encontra no 3° quadrante")
else:
    print("O ponto se encontra no 4° quadrante")