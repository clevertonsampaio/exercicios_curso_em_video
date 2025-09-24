from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*13)
print('Computador jogou \033[33m{}\033[m '.format(item[comp]))
print('Jogador    jogou \033[33m{}\033[m '.format(item[jogador]))
print('-='*13)
if comp == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA! ')
elif comp == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA! ')
elif comp == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA! ')
