from random import choice
a = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a, a2, a3, a4]
# [] serve para fazer lista .
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))
