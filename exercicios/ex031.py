dis = float(input('Qual a distancia da viagem ? '))
print('Você esta prestes a começar uma viagem de {}Km. '.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua apassagem séra de R${:.2f}'.format(preço))
