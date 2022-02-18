#DESAFIO 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite o valor em METROS que deseja converter: '))
cm = m * 100
mm = m * 1000
print(f'{m}m é igual a {cm:.0f}cm e {mm:.0f}mm.')