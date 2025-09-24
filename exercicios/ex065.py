res = 'S'
soma = quant = media = maior= menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if menor >= num:
            menor = num
        else:
            maior = num
    res = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} números e a média foi {media}')
print(f'O maior numero digitado foi {maior} e o menor foi {menor}.')