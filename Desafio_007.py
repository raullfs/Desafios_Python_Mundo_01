#DESAFIO 007
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
print(f'''Suas notas foram {nota1} e {nota2}.
A média entre elas é {media:.1f}.''')