aluno = {}
aluno['nome'] = str(input('Nome: ')).title()
aluno['nota'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['nota'] <= 5:
    aluno['situação'] = 'reprovada'
elif aluno['nota'] <= 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'Aprovada'
print('-=' * 22)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')


'''print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['nota']}')
print(f'Situação é igual a {aluno["situação"]}')'''
