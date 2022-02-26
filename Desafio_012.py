#DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Digite o preço do produto: R$'))
desc = prod - (prod * 5 / 100)
print(f'''O produto custa R${prod:.2f}
Com 5% de desconto custará R${desc:.2f}.''')