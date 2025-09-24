s = 0
con = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    d = n % 2
    if d == 0:
        s += n
        con = con + 1
print('A soma entre os numeros PARES é de {}'.format(s))
print(con)