def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa / 100)
    if formato:
        res=moeda(res)
    return res


def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa / 100)
    if formato:
        res=moeda(res)
    return res


def dobro(preço = 0, formato = False):
    res = preço * 2
    if formato:
        res=moeda(res)
    return res



def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def metade(preço = 0, formato = False):
    res = preço / 2
    if formato:
        res=moeda(res)
    return res

def resumo(preço=0, aumento=10, redução=5):
    print('-' * 30)
    #print(f'{"REESUMO DO VALOR":^30}')
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço):>11}')
    #print(f'Dobro do preço:  {dobro(preço,True):>11}'
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True):>11}')
    print(f'{aumento}% de aumento:  {aumentar(preço,aumento, True):>11}')
    print(f'{redução}% de redução:  {diminuir(preço,redução,True):>11}')
    print('-' * 30)