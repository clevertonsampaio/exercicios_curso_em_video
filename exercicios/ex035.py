print('\033[33;1m-=-\033[m' * 10)
print('\033[32;1mAnalisandorr de Triângulo\033[m')
print('\033[33;1m-=-\033[m' * 10)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m Triângulo')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m Triângulo')
