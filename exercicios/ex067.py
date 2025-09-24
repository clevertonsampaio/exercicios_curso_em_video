print('_' * 30)
print('\033[31mPROGRAMA DE TABUADA.\033[m')
while True:
      print('_' * 33)
      n = int(input('Quer ver a tabuada de quak valor? '))
      print('_' * 33)
      if n < 0:
          break
      for c in range(1, 11):
          print(f'{n:2} x {c:2} = {n*c:2}')
print('\033[31mPROGRAMA  TABUADA ENCERRADO.\033[32m Volte sempre')
