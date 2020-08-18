# Faça um programa que execute a lógica de cálculo de preços em um caixa. Seu programa receberá do usuário dois valores inteiros, 
# o primeiro é correspondente ao código do produto a ser comprado, o segundo valor é a quantidade desse item. 
# Utilizando as instruções adiante, calcule o preço total da compra.
# O produto de código 1 custa R$ 4.00, o produto de código 2 custa R$ 4.50, o produto de código 3 custa R$ 5.00
# o produto de código 4 custa R$ 2.00, o produto de código 5 custa R$ 1.50. 
# Caso o código do produto não se encaixe em nenhuma das possibilidades citadas, imprima na tela uma mensagem de erro ao usuário.

codigo = int(input("Insira o código do produto: "))
quantidade = int(input("Insira a quantidade do produto: "))
valores = [4.00, 4.50, 5.00, 2.00, 1.50]

if codigo < 1 or codigo > 5:
    print("\nErro! Produto não cadastrado!")
else:
    print(f"\nPreço total da compra é de: R$ {valores[codigo-1]*quantidade}")