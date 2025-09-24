a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificar queem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O \033[33mmenor\033[m valor digitado foi \033[33m{}\033[m'.format(menor))
print('O \033[31mmaior\033[m valor digitado foi \033[31m{}\033[m'.format(maior))
