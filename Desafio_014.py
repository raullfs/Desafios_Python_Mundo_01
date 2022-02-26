#DESAFIO 014
#Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em °C: '))
f = (c * 9 / 5) + 32
print(f'A temperatura de {c}°C convertida para fahrenheit será de {f}°F.')