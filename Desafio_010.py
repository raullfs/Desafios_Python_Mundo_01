# DESAFIO 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1.00 = R$3.27

real = float(input('Informe quantos R$ você tem: R$'))
dolar = 3.27
conversao = real / dolar
print(f'Com R${real:.2f} você consegue comprar US${conversao:.2f}.')