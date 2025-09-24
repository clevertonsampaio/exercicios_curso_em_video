numero = ('Zero', 'Um', 'Dois', 'Tres','Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('tente novamente ', end='')
print(f'Você digitou o numero {numero[escolha]}')
