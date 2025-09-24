lis = []
while True:
    n = int(input('digite um numero :'))
    if n not in lis:
        lis.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Deseja continuar [S]SIM / [N]NÃO :')).upper()[0]
    if res in 'Nn':
        break
print('-=' * 30)
lis.sort()
print(f'Voce digitou os valores {lis}')
