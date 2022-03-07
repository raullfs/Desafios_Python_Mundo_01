primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo = termo + razao
        cont = cont + 1
    print('')
    mais = int(input('Informe a quantidade de termos que deseja verificar a mais: '))
print('Até logo')