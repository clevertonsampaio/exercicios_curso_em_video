list = []
par = []
impar = []
while True:
    list.append(int(input('Digite um valor: ')))
    res = str(input('Deseja parar ? [S/N] ')).upper()[0]
    if res in 'S':
        break
for pos, v in enumerate(list):
    #if v % 2 == 0:
    #   par.append(v)
    if list[pos] % 2 == 0:
        par.append(v)
    elif list[pos] % 2 == 1:
        impar.append(v)
list.sort()
par.sort()
impar.sort()
print(f'a lista digitada foi {list}')
print(f'os numeros pares digitados foram {par}')
print(f'os valores impar digitados foram {impar}')
