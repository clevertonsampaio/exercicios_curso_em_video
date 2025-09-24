valor = []
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor {cont+1}: ')))
max = max(valor)
min = min(valor)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max} nas posiçoes ', end=' ')
for c, val in enumerate(valor):
    if val == max:
        print(f'{c+1}...', end=' ')
print(f'\nO menor valor digitado foi {min} nas posiçoes ', end=' ')
for c, val in enumerate(valor):
    if val == min:
        print(f'{c+1}...', end=' ')
print()
