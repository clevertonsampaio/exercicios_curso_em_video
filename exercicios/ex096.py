def area(a,b):
    s = a * b
    print(f'A area de um terreno {a} X {b} é de {s}m².')


print('  CONTROLE DE TERRENO ')
print('--' * 20)
l = float(input('Largura (m)'))
c = float(input('Comprimento (m)'))
area(l,c)
