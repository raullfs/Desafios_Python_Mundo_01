jogador = {}
partida = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partida.append((int(input(f'    Quantos gols na partida {c + 1}? '))))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    >> Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')