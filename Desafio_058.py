from random import randint
cont = 1
computador = randint(0,10)
print('Tente adivinhar o número que pensei:')
jogar = int(input('Digite seu palpite: '))
while computador != jogar:
    if computador > jogar:
        print('MAIS... Você errou, tente novamente.', end=' ')
    else:
        print('MENOS... Você errou, tente novamente.', end=' ')
    jogar = int(input('Digite seu palpite: '))
    cont = cont + 1
print(f'Você acertou na {cont}° tentativa.')