#DESAFIO 011
#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area / 2
print(f'Sua parede tem {area:.1f}m² e será necessário {tinta:.1f}L de tinta.')