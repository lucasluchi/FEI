# Faça um programa que realize a leitura de três notas parciais de um aluno e calcule a média 
# (M = (N1 + N2*2 + N3*3)/6) alcançada pelo aluno e apresentar: 
# A mensagem "Aprovado", se a média for maior ou igual a 5, com a respectiva média alcançada; 
# A mensagem "Reprovado", se a média for menor do que 5, com a respectiva média alcançada;

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

media = round((nota1 + nota2 * 2 + nota3 * 3)/6, 2)
condicao = "reprovado"

if media >= 5.00:
    condicao = "aprovado"

print(f"Aluno {condicao} - Média: {media:.2f}")