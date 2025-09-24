from random import shuffle
a = input('Primeiro(a) aluno(a) : ')
a2 = input('Segundo(a) aluno(a) : ')
a3 = input('Terceiro(a) aluno(a) : ')
a4 = input('Quarto(a) aluno(a) : ')
lista = [a, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
