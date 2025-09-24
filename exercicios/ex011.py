# faça um programa que leia a largura e a altura de uma parede em metros , calcule
# a sua area e a quantidade necessaria para pinta-lo sabendo que cada litro
# de tinta pinta uma area de 2m²
a = float(input('Digite a altura da parede : '))
l = float(input('Digite a largura da parede : '))
s = a * l
t = s / 2
#print('sabendo que a parede tem {}m² sabemos que precisamos de {}l de tinta!'.format(s, t))
print('sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(a, l, s))
print('para pintar essa parede, você precisará de {}l de tinta.'.format(t))
