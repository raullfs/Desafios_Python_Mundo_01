#DESAFIO 017
#Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import *
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')