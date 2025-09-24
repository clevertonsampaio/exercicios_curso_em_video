print('Gerador de PA')
print('\033[35m-=\033[m' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = primeiro
cont = 1
print('\033[35m-=\033[m' * 10)
print('')
print('')
print('\033[35m-=\033[m' * 37)
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end=' ')
        termo += raz
        cont += 1
    print('PAUSA')
    print('\033[35m-=\033[m' * 37)
    mais = int(input('Quantos termos vovê quer mostrar a mais ? '))
print(f'Progressão finalizada com \033[31m{total}\033[m termos mostrados.')
