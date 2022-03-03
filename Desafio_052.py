num = int(input('Informe um número: '))
primo = 0
for c in range(1, num + 1):
    if num % c == 0:
        primo = primo + 1
if primo == 2:
    print(f'O número {num} é um número PRIMO, ele foi divisível {primo} vezes.')
else:
    print(f'O número {num} NÃO é um número PRIMO, ele foi divisível {primo} vezes.')