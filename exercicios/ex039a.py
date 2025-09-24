from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
print('''Qual seu sexo
[1] Masculino
[2] Femenino''')
opcao = int(input('qual sua opção:'))
print('')
if opcao == 1:
    if idade == 18:
      print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento sera em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos .'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif opcao == 2:
    print('Voce não é obrigada a se alistar.')
