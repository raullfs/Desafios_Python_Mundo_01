from random import randint
lista = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)
print('''Escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('>>>>> '))
print(f'O computador escolheu {lista[comp]} e você escolheu {lista[opcao]}.')
if comp == 0:
    if opcao == 0:
        print('EMPATOU')
    elif opcao == 1:
        print('Você GANHOU')
    elif opcao == 2:
        print('Você PERDEU')
elif comp == 1:
    if opcao == 0:
        print('Você PERDEU')
    elif opcao == 1:
        print('EMPATOU')
    elif opcao == 2:
        print('Você GANHOU')
elif comp == 2:
    if opcao == 0:
        print('Você GANHOU')
    elif opcao == 1:
        print('Você PERDEU')
    elif opcao == 2:
        print('EMPATOU')