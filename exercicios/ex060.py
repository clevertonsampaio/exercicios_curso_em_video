n = int(input('Digite um numero: '))
f = 1
c = n
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'verme': '\033[31m',
        'amarelo': '\033[33m',
         'azul': '\033[34m'}
print(f'{cores['azul']}calculando {n}! =', end=' ')
while c > 0:
    print(f'{cores['verde']} {c} {cores['limpa']}', end=' ')
    print(f'{cores['amarelo']} X {cores['limpa']}' if c > 1 else f'{cores['amarelo']} = {cores['limpa']}', end=' ')
    f *= c
    c -= 1
print(cores['verme'], f, cores['limpa'])
