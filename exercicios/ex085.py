final = [[], []]
for con in range(1,8):
    n = int(input(f'digite o {con}º valor: '))
    if n % 2 == 0: #par
        final[0].append(n)
    elif n % 2 == 1:
        final[1].append(n)
final[0].sort()
final[1].sort()
print(f'Os valores pares digitados foram: {final[0]}')
print(f'Os valores impares digitados foram:  {final[1]}')
