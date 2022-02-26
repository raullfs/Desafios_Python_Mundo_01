#DESAFIO 015
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de KM percorrida: '))
diaria = int(input('Informe por quantos dias foi alugado: '))
total = (km * 0.15) + (diaria * 60)
print(f'''Você alugou o carro por {diaria} dias
Você percorreu {km:.0f}km
O total do aluguel é R${total:.2f}''')