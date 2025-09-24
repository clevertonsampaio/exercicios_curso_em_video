casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
por = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de {:.2f}'.format(prestacao))
if prestacao <= por:
    print('Emprestimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print('Emprestimo \033[31mNEGADO!\033[m')
print('O valor maximo que pode atingir é de R${:.2f}'.format(por))
