kg = float(input('Qual é seu peso? (Kg)'))
med = float(input('Qual é sua altura ? (M)'))
imc = kg / (med ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 17:
    print('Voce esta MUITO ABAIXO do peso ')
elif imc < 18.5:
    print('Voce esta ABAIXO DO PESO ')
elif imc < 25:
    print('Voce esta no PESO ideal ')
elif imc < 30:
    print('Voce esta no SOBREPESSO ')
elif imc < 35:
    print('Voce esta com OBSEIDADE , Cuidado')
elif imc < 40:
    print('Voce esta na OBSIDADE SEVERA , MUITO CUIDADO')
else:
    print('Voce esta na OBSEDADE MÓRBIDA. MUITA ATENÇÃO')
