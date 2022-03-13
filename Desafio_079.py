lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado.', end=' ')
    sair = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if sair == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')