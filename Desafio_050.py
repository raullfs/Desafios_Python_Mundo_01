soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Informe o {c}° número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você informou {cont} números pares e a soma entre eles é igual a {soma}.')