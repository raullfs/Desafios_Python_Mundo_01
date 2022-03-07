idade_total = cont = idade_fem = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: ')).upper().strip()[0]
    if idade >= 18:
        idade_total += 1
    if sexo == 'M':
        cont += 1
    if sexo == 'F' and idade < 20:
        idade_fem += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {idade_total}
Ao todo temos {cont} homens cadastrados
E temos {idade_fem} mulheres com menos de 20 anos.''')
