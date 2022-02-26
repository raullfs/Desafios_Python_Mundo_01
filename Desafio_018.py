#DESAFIO 018
#Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

from math import *
angulo = float(input('Informe um angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'''Você informou um angulo de {angulo:.0f}°.
O seno é igual a {sen:.2f}
O cosseno é igual a {cos:.2f}
A tangente é igual a {tan:.2f}.''')