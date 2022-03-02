a = float(input('Informe o 1° segmento: '))
b = float(input('Informe o 2° segmento: '))
c = float(input('Informe o 3° segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos informados formam um TRIÂNGULO', end=' ')
else:
    print('Os segmentos informados NÃO formam TRIÂNGULO!')
if a == b and b == c:
    print('EQUILÁTERO')
elif a != b and b != c and c != a:
    print('ESCALENO')
else:
    print('ISÓSCELES')