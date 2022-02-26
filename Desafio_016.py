#DESAFIO 016
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import *
num = float(input('Digite um número real: '))
print(f'O número real informado foi {num} e sua porção inteira é {trunc(num)}.')