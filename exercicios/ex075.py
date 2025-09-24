num = (int(input('Digite um numero ')),
        int(input('Digite outro numero ')),
        int(input('Digite mais um numero ')),
        int(input('Digite o ultimo numero ')))
print(f'Voce digitou os valoress {num}')
if 9 in num:
        print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
        print('Não foi digitado nenhum 9! ')
if 3 in num:
        print(f'O valor 3 foi digitado na posição {num.index(3)+1}°')
else:
        print('O valor 3 não foi digitado em nenhuma posição ')
print('Os valores pares digitados foram ', end='')
for n in num:
        if n % 2 == 0:
                print(n, end=' ')
