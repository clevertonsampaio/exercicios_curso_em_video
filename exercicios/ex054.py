from datetime import date
novo = 0
velho = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu?'))
    idade = atual - ano
    if idade <= 21:
        novo += 1
    else:
        velho += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE tambem tivemos {} pessoas menores de idade'.format(velho, novo))