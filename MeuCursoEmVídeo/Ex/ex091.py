from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for c in range(0, 4):
    jogadores[f'{c}'] = randint(1, 6)
sleep(0.8)
ranking = {}
for k, v in jogadores.items():
    print(f'O {int(k)+1}º jogou: {v}.')
    sleep(0.75)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('CLASSIFICAÇÃO')
sleep(0.8)
for k, v in enumerate(ranking):
    print(f'O {int(v[0])+1}º jogador jogou {v[1]} e ficou em {k+1}.')
    sleep(0.75)