from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(' ')
    print('\033[35m=-=\033[m' * 10)
    print('''    \033[33m[1]\033[m SOMAR
    \033[33m[2]\033[m MULTIPLICAR
    \033[33m[3]\033[m MAIOR
    \033[33m[4]\033[m NOVO NÚMEROS
    \033[33m[5]\033[m SAIR DO PROGRAMA''')
    print('\033[35m=-=\033[m' * 10)
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é equivalente a {s} !')
    elif opcao == 2:
        s = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é equivalente a {s} !')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior} !')
    elif opcao == 4:
        n1 = int(input('Digite primeiro valor:'))
        n2 = int(input('Digite  segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção invalida tente novamente!')
print('\033[32mFim do programa! Volte sempre!')
