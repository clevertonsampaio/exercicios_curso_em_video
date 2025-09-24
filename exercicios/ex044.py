print('{:=^40}'.format(' OHANA '))
valor = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[1] á vista dinheiro /cheque
[2] á vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
pa = int(input('Qual é  a opção? '))
if pa == 1:
    des = valor - (valor * 10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, des))
elif pa == 2:
    des = valor - (valor * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, des))
elif pa == 3:
    des = valor / 2
    print('A conta de R${:.2f} ficara 2x de R${:.2f} SEM JUROS '.format(valor, des))
elif pa == 4:
    par = int(input('Quantas parcelas ? '))
    des = valor + (valor * 20/100)
    di = des / par
    print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS
    Sua compra de R${:.2f} vai custar R${:.2f} no final'''.format(par, di, valor, des))
