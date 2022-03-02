prod = float(input('Informe o valor do produto: R$'))
print('''Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('>>>>> '))
if opcao == 1:
    desc = prod - (prod * 10 / 100)
    print(f'O preço final do seu produto será: R${desc:.2f}')
elif opcao == 2:
    desc = prod - (prod * 5 / 100)
    print(f'O preço final do seu produto será: R${desc:.2f}')
elif opcao == 3:
    parc = prod / 2
    print(f'O preço final do seu produto será: 2x R${parc:.2f}')
elif opcao == 4:
    prod = prod + (prod * 20 / 100)
    parc = int(input('Informe a quantidade de parcela: '))
    total = prod / parc
    print(f'O preço final do seu produto será: {parc}x R${total:.2f}')