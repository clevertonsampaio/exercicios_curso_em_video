def leiaInt(msg):
    import color
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{color.vermelho()}ERRO! Digite um numero inteiro válido.{color.remover()}')
        if ok:
            break
    return valor

#programa principal
n = leiaInt('digite um número: ')
print(f'Você acabou de digitar o número {n}')