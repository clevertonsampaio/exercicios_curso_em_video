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