#DESAFIO 013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o salário do funcionário: R$'))
aum = sal + (sal * 15 / 100)
print(f'''O funcionário tem o salário de R${sal:.2f}
Com o reajuste de 15% passara a receber R${aum:.2f}''')
