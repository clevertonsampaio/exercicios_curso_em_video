listagem = ('lapis', 2,
            'borracha', 2.5,
            'caderno', 17.5,
            'estojo', 27,
            'trasferidor', 4.5,
            'compasso', 9.99,
            'mochila', 125.35,
            'caneta', 20.0,
            'livro', 35.75)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:7.2f}')
print('-' * 40)
