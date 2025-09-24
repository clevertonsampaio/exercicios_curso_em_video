# CONVERTER REAL EM DOLAR
n = float(input('quantos em real você tem ? R$'))
s = n / 5.25
print('O valor R${} convertido em dolar fiaca US${:.2f}'.format(n, s))
e = n / 5.69
i = n / 0.033
print('Com R${} convertido em euro fica EUR${:.2f}'.format(n, e))
print('Com R${} convertido em iene fica JPY${:.2f}'.format(n, i))
