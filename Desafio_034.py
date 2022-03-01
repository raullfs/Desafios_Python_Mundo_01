sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250:
    print(f'Seu salário passou de R${sal:.2f} para R${sal + (sal * 10 / 100):.2f}')
else:
    print(f'Seu salário passou de R${sal:.2f} para R${sal + (sal * 15 / 100):.2f}')