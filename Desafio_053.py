frase = str(input('Digite a frase que deseja verificar: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverte = ''
for c in range(len(junta) -1, -1, -1):
    inverte = inverte + junta[c]
if inverte == junta:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} NÃO é um palíndromo.')