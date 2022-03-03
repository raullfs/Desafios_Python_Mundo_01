num = int(input('Digite um número: '))
c = num
fac = 1
print(f'{num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fac = fac * c
    c = c - 1
print(f'{fac}')