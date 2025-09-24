import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
h = (n1*n1) + (n2*n2)
#y = math.sqrt(h)
y = math.hypot(n1, n2)
print('A hipotenusa calcullando pelos valores {} , {} vale {:.2f}'.format(n1, n2, y))
