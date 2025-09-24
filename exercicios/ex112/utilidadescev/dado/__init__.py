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
