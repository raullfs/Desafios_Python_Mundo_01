#DESAFIO 020
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import *
aluno1 = str(input('Informe o nome do 1° aluno: '))
aluno2 = str(input('Informe o nome do 2° aluno: '))
aluno3 = str(input('Informe o nome do 3° aluno: '))
aluno4 = str(input('Informe o nome do 4° aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'''A ordem da apresentação será: 
{alunos}''')