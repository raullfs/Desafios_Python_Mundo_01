a = float(input('Digite o 1° segmento: '))
b = float(input('Digite o 2° segmento: '))
c = float(input('Digite o 3° segmento: '))
if a < b + c and b < a + b and c < a + b:
    print('Os segmentos informados PODEM formar um triângulo!')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo!')