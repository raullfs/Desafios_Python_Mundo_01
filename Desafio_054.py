from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano do nascimento da {c}° pessoa: '))
    idade = atual - nasc
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')