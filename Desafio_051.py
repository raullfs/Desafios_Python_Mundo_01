termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
dez = termo + (10 - 1) * razao
for c in range(termo, dez + razao, razao):
    print(c, end=' ')
