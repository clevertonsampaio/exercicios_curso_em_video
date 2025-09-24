jogador = {}
partida = []
jogador['nome'] = str(input('Qual o nome do jogador : '))
tot = int(input(f'quantas partidas o {jogador["nome"]} jogoou :'))
for c in range(0, tot):
    partida.append(int(input(f'quantos gols foi feito na partida {c+1} :')))
jogador['gols'] = partida
jogador['total'] = sum(partida)
print('=-'*30)
print(jogador)
print('=-'*30)
partida.clear()
for c, v in jogador.items():
    print(f'  -O campo {c} tem o valor {v} ')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas')
for c, v in enumerate(jogador['gols']):
    print(f'  => Na partida {c+1}, fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')
print('-='*30)
print(partida)