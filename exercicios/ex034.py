'''sala = float(input('Qual o valor do salário: '))
if sala <= 1.250:
    aum = sala * 15 / 100
else:
    aum = sala * 10 / 100
print(aum+sala)'''
salario = float(input('Qual é o salario do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava \033[1;31mR${:.2f}\033[m passa a ganhar \033[1;32mR${:.2f}\033[m agora. '.format(salario, novo))
