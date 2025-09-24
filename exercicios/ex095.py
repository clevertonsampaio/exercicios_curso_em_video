time = list()
jogador = {}
partida = []

while True:
    partida.clear()
    jogador['nome'] = str(input('Qual o nome do jogador : '))
    tot = int(input(f'quantas partidas o {jogador["nome"]} jogou :'))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'quantos gols foi feito na partida {c+1} :')))
    jogador['gols'] = partida
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Resposta apenas S ou N. ')
    if resp == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No Jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
