# exercicios/ex005.py
# Programa que lê um número inteiro e mostra o seu antecessor e sucessor

# .format() é um método que formata o texto
# {} é um espaço reservado para o valor que será inserido no texto

n1 = int(input('Digite um numero: '))
print('O atecessor de {} é igual a {} e o seusucessor é {} !'.format(n1, n1-1, n1+1))

