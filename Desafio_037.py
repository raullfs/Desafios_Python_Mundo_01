num = int(input('Digite um número: '))
print('''Escolha uma opção:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('>>>>> '))
if opcao == 1:
    print(f'O número {num} convertido para binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para binário é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para binário é: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')