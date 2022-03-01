km = float(input('Informe quantos KM tem a sua viagem: '))
if km <= 200:
    print(f'Sua viagem tem {km:.0f}km e custará R${km * 0.50:.2f}')
else:
    print(f'Sua viagem tem {km:.0f}km e custará R${km * 0.45:.2f}')