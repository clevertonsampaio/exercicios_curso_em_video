nume = int(input('Digite um numero :'))
u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 1000 % 10
print('Analisando o numero {}'.format(nume))
print('Unidade: {} '.format(u))
print('Dezena : {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar : {} '.format(m))

