from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado. ')
    sleep(1)
print('-=' * 30)
sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==')
for i, n in enumerate(ranking):
    print(f'   {i+1}° ficou o {n[0]} com {n[1]}')
    sleep(1)
