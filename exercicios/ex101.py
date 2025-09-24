def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Não vota .'
    elif 16 < idade < 18 or idade > 65:
        return f'com {idade} anos: voto opcional.'
    else:
        return f'com {idade} anos: voto obrigatorio.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
