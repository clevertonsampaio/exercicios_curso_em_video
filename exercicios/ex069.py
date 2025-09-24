total = totalh = total20 = 0
cores = {'limpa':'\033[m',
         'verm':'\033[31m',
         'verd':'\033[32'}
while True:
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade >= 18:
        total += 1
    if sexo == 'F' and idade <= 20:
        total20 += 1
    if sexo == 'M':
        totalh += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'conteve {cores['verm']}{total}{cores['limpa']} de pessoas com mais de 18 anos')
print(f'conteve {cores['verm']}{totalh}{cores['limpa']} homens cadastrado')
print(f'conteve {cores['verm']}{total20}{cores['limpa']} mulheres com menos de 20 anos')