num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {num}' )
print(f'O maior valor digitado foi {max(num)} nas posições', end=' ')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(num)} nas posições', end=' ')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}... ', end='')
