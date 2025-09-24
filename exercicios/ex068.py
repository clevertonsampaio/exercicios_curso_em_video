from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P / I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
    print('\033[32mDEU PAR \033[m' if total % 2 == 0 else '\033[32mDEU IMPAR\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32mVENCEU\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[32mVENCEU\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU\033[m')
            break
    print('vamos jogar novamente...')
print(f'\033[31mGAME OVER!\033[m Você venceu \033[34m{v}\033[m vezes cosecultiva.')
