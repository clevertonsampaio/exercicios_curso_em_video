from util import moeda
num = float(input('Digite o preço: R$'))
print(f'A metade de R${num:.2f} é R${moeda.metade(num):.1f}')
print(f'O dobro de R${num:.2f} é R${moeda.dobro(num):.1f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10):.1f}')