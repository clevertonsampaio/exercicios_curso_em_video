n1 = float(input('Digite uma metragem: '))
dm = n1 * 10
c = n1 * 100
mm = n1 * 1000
km = n1 / 1000
hm = n1 / 100
da = n1 / 10
#print('Tendo {}m é o mesmo de {:.0f}cm e o mesmo de {:.0f}mm !'.format(n1, c, mm))
print('A medida de {:.1f}m corresponde a '.format(n1))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{:.1f}dam'.format(da))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(c))
print('{:.0f}mm'.format(mm))

