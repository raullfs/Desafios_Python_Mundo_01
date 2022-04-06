from random import *
from time import *
from operator import *
jogador = {'Jogador_1': randint(1, 6),
           'Jogador_2': randint(1, 6),
           'Jogador_3': randint(1, 6),
           'Jogador_4': randint(1, 6)}
ranking = {}
for k, v in jogador.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('===== RANKING FINAL =====')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)