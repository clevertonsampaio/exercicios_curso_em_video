def maior(* num):
    from time import sleep
    print('Analizando valores...')
    cont = maior = 0
    print('-=' * 20)
    for valor in num:
        print(f'{valor} ', end='',flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foran informado {cont} valores ao todo ')
    print(f'o maior valor informado foi {maior}. ')


#programa principal
maior(1,3,5,7,9)