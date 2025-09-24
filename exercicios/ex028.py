from random import randint
num = randint(0, 5)
num2 = int(input('Vou pensar em um numero entre 0 e 5. tente adivinhar:'))
if num == num2:
    print('Parabens por acerta o numero')
else:
    print('Que triste você errou :')

print(num)
