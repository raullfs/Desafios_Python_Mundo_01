termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ')
    termo = termo + razao
    cont = cont + 1
