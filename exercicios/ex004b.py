# exercicios/ex004b.py
# Programa que lê algo digitado pelo usuário e mostra várias informações sobre ele

# type() mostra o tipo primitivo do valor
# isspace() mostra se é só espaço
# isnumeric() mostra se é um número
# isalpha() mostra se é alfabético
# isalnum() mostra se é alfanumérico
# istitle() mostra se está capitalizada
# isupper() mostra se tem apenas letras maiúsculas
# islower() mostra se tem apenas letras minúsculas
# len() mostra o tamanho do valor

a = input('Digite algo: ')
print('O tipo primitivo desse valor é : ', type(a))
print('So tem espaços? :', a.isspace())
print('É um numero? :', a.isnumeric())
print('É alfabético? :', a.isalpha())
print('É alfanumerico? :', a.isalnum())
print('esta capitalizada? :', a.istitle())
print('Tem apenas letras maiuscula? :', a.isupper())
print('Tem apenas letras minusculas? :', a.islower())
