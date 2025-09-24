n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f} '.format(n1, n2, s))
if s < 5:
    print('O aluno esta \033[31mREPROVADO\033[m')
elif 7 > s >= 5:
#elif s > 5 and s < 6.9:
    print('O aluno esta em \033[33mRECUPERAÇÃO\033[m')
elif s > 7:
    print('O aluno esta \033[32mAPROVADO\033[m')
