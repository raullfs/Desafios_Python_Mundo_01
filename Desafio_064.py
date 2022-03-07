num = 0
cont = 0
soma = 0
print('===> Para sair digite 999')
num = int(input('Digite um número: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')