from time import sleep
num1 = int(input('Informe o 1° número: '))
num2 = int(input('Informe o 2° número: '))
opcao = 0
while opcao != 5:
    print('''Informe a opção desejada:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> '))
    if opcao == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif opcao == 2:
        multi = num1 * num2
        print(f'{num1} x {num2} = {multi}')
    elif opcao == 3:
        if num1 == num2:
            print(f'Os números são iguais.')
        elif num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O número {maior} é o maior número entre {num1} e {num2}.')
    elif opcao == 4:
        num1 = int(input('Informe o 1° número: '))
        num2 = int(input('Informe o 2° número: '))
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(1)
print('Até logo!')