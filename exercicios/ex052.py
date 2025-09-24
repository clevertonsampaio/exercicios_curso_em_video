n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero \033[36m{}\033[m foi divisivel \033[36m{}\033[m vezes '.format(n, tot))
if tot == 2:
    print('E por isso ele é \033[32mPRIMO!')
else:
    print('E por isso ele \033[32mNÃO É PRIMO!')
