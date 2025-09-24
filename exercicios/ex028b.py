from random import randint
from time import sleep
pc = randint(0, 5)
print('\033[1;36m-=-\033[m' *20)
print('\033[1;34mVou pensar em um número entre 0 e 5. tente adivinhar...')
print('\033[1;36m-=-\033[m'*20)
jogador = int(input('Em que numero eu pensei? :'))
print('PROCESSANDO...')
sleep(0.8)
print('PROCESSANDO...')
sleep(0.5)
if jogador == pc:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('\033[34mGANHEI!\033[m Eu pensei no numero {} e nao o {}!'.format(pc, jogador))
