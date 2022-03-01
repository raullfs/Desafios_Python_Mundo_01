from random import randint
pc = randint(0, 5)
play = int(input('Informe um número entre 0 e 5: '))
print(f'O computador pensou no número {pc} e você informou o número {play}')
if pc == play:
    print('O jogador VENCEU!')
else:
    print('O jogador Perdeu!')
