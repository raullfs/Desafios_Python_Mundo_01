#DESAFIO 019
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import *
aluno1 = str(input('Informe o nome do 1° aluno: '))
aluno2 = str(input('Informe o nome do 2° aluno: '))
aluno3 = str(input('Informe o nome do 3° aluno: '))
aluno4 = str(input('Informe o nome do 4° aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno sorteado foi {choice(alunos)}.')