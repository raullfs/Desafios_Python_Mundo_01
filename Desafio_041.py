from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de seu nascimento: '))
idade = atual - nasc
print(f'Você tem {idade} anos, sua categoria é:', end=' ')
if idade <= 9:
    print('MIRIM!')
elif idade <= 14:
    print('INFANTIL!')
elif idade <= 19:
    print('JÚNIOR!')
elif idade <= 25:
    print('SÊNIOR!')
else:
    print('MASTER!')