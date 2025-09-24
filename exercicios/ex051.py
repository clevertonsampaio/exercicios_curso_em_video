p = int(input('Primeira termo: '))
r = int(input('Razão: '))
de = p + (10 - 1) * r
for c in range(p, de + r, r):
    print(c, end=' ')
print('ACABOU ')