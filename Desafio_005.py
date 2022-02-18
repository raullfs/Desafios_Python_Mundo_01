#DESAFIO 005
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1
print(f'Você digitou o número {num}, o seu antecessor é o número {ant} e seu sucessor é o número {suc}.')