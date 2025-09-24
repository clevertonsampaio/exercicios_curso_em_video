def leiadinheiro(msg):
    from util import cores
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() 
        if entrada.isalpha() or entrada == '' :
            print(f'{cores.vermelho()}ERRO: \"{entrada}\" é um preço inválido!{cores.remover()}')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    from util import cores
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores.vermelho()}ERRO! Digite um numero inteiro válido.{cores.remover()}')
        if ok:
            break
    return valor