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
while cont <= 10:
    print(f'{termo} -> ', end=' ')
    termo += raz
    cont += 1
print('FIM')
print('\033[35m-=\033[35m' * 37)
