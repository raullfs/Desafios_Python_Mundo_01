from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano do seu nascimento: '))
idade = atual - nasc
if idade < 18:
    alist = 18 - idade
    print(f'Ainda faltam {alist} anos para seu alistamento.')
    print(f'Seu alistamento será em {nasc + 18}.')
elif idade == 18:
    print(f'Você já tem {idade} anos e deve se alistar este ano.')
else:
    alist = idade - 18
    print(f'Você tem {idade} anos e deveria ter se alistado a {alist} anos atrás. ')
    print(f'Seu alistamento foi em {nasc + 18}.')