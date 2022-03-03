soma = 0
media = 0
idademv = 0
nomemv = ''
mulher = 0
for c in range(1, 5):
    print(f'Informação da {c} pessoa:')
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input(f'Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    soma = soma + idade
    media = soma / 4
    if c == 1 and sexo == 'M':
        idademv = idade
        nomemv = nome
    if sexo in 'M' and idade > idademv:
        idademv = idade
        nomemv  = nome
    if sexo in 'F' and idade < 20:
        mulher = mulher + 1
print(f'A media de idade é de {media} anos.')
print(f'O homem mais velho tem {idademv} anos e seu nome é {nomemv}.')
print(f'Foram localizados {mulher} registros do sexo FEMININO inferior a 20 anos.')