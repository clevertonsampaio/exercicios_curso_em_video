from random import randint
computador = randint(0, 10)
print('''Sou seu Computador... Acabei de pensar em um número entre 0 e 10.
Sera que você consegue adivinhar qual foi?''')
acertou = False
palpites = 0
while not acertou:
   jogador = int(input('Qual é seu palpite? '))
   palpites += 1
   if jogador == computador:
       acertou = True
   else:
       if jogador < computador:
           print('Mais... Tente mais uma vez.')
       elif jogador > computador:
           print('Menos... Tente mais uma vez.')
if palpites <= 4:
    print(f'Acertou com {palpites} tentativas. Parabéns!')
elif palpites > 4 and palpites < 6:
    print(f'Acertou com {palpites} tentativas. parabéns más podia melhorar!')
else:
    print(f'Acertou com {palpites} tentativas. Não foi tão bem!')