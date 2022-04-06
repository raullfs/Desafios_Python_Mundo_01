lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    sair = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if sair == 'N':
        break
print(f'''A lista completa é {lista}
A lista de pares é {par}
A lista de impares é {impar}''')
