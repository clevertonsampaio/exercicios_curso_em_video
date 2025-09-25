# exercicios/ex006.py
# Programa que lê um número e mostra o seu dobro, triplo e raiz quadrada

# ** é o operador de potência
# \n é o caractere de nova linha (quebra de linha)

n = int(input('Digite um  numero: '))
#print('O dobro de {} é {} \nSeu triplo é {} \nE sua raiz quadrada é {:.2f} !'.format(n, n*2, n*3, n**(1/2)))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, d, n, t, n, r))