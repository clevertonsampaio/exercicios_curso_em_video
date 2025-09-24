from datetime import date
atual = date.today().year
nasc = int(input('qual a data do seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} no ano {} tem {} anos '.format(nasc, atual, idade))
'''if idade <= 9:
    print('a criança é da faixa mirim')
elif idade > 9 and idade < 14:
    print('A criança é da faixa infantil')
elif idade > 14 and idade < 19:
    print('a pessoa ja é da faixa junior ')
elif idade > 19 and idade < 25:
    print('a pessoa ja é da faixa sênio')
else:
    print('O competidor ja é um candidato master')'''
if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior')
elif idade <= 25:
    print('senior')
else:
    print('master')
