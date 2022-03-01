vel = int(input('Informe sua velocidade: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Você esta dentro do limite de velocidade.')
else:
    print(f'Você ultrapassou o limite de velocidade, sua multa será de R${multa:.2f}!')