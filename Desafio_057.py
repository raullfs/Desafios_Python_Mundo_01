sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dados invalídos, Tente novamente.', end=' ')
    sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} inserido com sucesso.')