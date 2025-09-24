'''import math, emoji
n = float(input('Digite um numero : '))
#a = math.floor(n)
a = math.trunc(n)
print(emoji.emojize('O numero {} tem a parte inteira {}! 📲'.format(n, a)))'''

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porçao inteira é {}'.format(n, int(n)))
