cont = soma = 0
print('Digite 999 para SAIR')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'A soma dos {cont} valores é {soma}.')
