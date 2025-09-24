ficha = []
while True:
    nome = str(input('Nome : ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1+n2)/2
    ficha.append([nome, [n1, n2], med])
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[2]:8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno ? (999 interompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
