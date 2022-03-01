frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'Em que posição ela aparece a primeira vez? Posição {frase.find("A")+1}')
print(f'Em que posição ela aparece a última vez? Posição {frase.rfind("A")+1}')