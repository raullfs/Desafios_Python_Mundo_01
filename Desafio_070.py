total = caro = menor = cont = 0
prod_bar = ''
while True:
    prod = str(input('Informe o produto: ')).strip().title()
    val = float(input('Informe o valor do produto: R$'))
    total += val
    cont += 1
    if val > 1000:
        caro += 1
    if cont == 1:
        menor = val
        prod_bar = prod
    else:
        if val < menor:
            menor = val
            prod_bar = prod
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if sair == "N":
       break
print(f'O valor total da compra é R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_bar} que custa R${menor:.2f}')