val = float(input('Informe o valor do imóvel: R$'))
sal = float(input('Informe a renda do comprador: R$'))
fin = int(input('Informe quantos anos de financiamento: '))
par = (val / fin) / 12
min = sal * 30 / 100
if par <= min:
    print(f'O financiamento pode ser APROVADO com a prestação de R${par:.2f}')
elif par > min:
    print(f'O financiamento foi NEGADO, prestação superior a 30% da renda.')