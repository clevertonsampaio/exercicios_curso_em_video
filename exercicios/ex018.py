from math import radians, sin, cos, tan
an = float(input('Digite o angulo que você deseja: '))
sen = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, sen))
coss = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, coss))
tan = tan(radians(an))
print('O angulo de {} trm a TANGENTE de {:.2f}'.format(an, tan))
