from random import randint
cont = 0
while True:
    pc = randint(1, 10)
    num = int(input('Digite um número: '))
    pi = str(input('Par ou Impar: ')).strip().upper()[0]
    result = pc + num
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Impar: ')).strip().upper()[0]
    print(f'Você jogou {num} e o computador {pc}. {result} É ', end='')
    if pi == 'P':
        if result % 2 == 0:
            print('PAR.')
            print('Você GANHOU.')
        else:
            print('ÍMPAR.')
            print('Você PERDEU.')
            break
    elif pi == 'I':
        if result % 2 == 1:
            print('PAR.')
            print('Você GANHOU.')
        else:
            print('ÍMPAR.')
            print('Você PERDEU')
            break
    cont += 1
print(f'GAME OVER! Você venceu {cont}')