def fatoria(n,show=False):
    """
    -> calcula o fatorial de um numero .
    :param n: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial de um numero n
    função criada por morvou
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print('X',end='')
            else:
                print('=', end='' )
        f *= c
    return f

