# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
n = float(input('Qual é o salario do funcionario? R$'))
s = n * 15 / 100
#print('Considerando que seu salario era R${:.2f} agora sera R${:.2f} !'.format(n, n+s))
print('Um funcionario que eganhava R${:.2f}, Com 15% de aumento passa a receberR${:.2f}'.format(n, n+s))