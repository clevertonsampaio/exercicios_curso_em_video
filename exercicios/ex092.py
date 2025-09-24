from datetime import date
clt = {}
clt['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
clt['idade'] = date.today().year - nasc
clt['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if clt['carteira'] != 0:
    clt['contratação'] = int(input('Ano de contratação: '))
    clt['salario'] = float(input('Salário: R$'))
    clt['aposentadoria'] = ((clt['contratação'] + 35) - date.today().year) + clt['idade']
print('-=' * 30)
for k, v in clt.items():
    print(f'  - {k} tem o valor de {v}')

