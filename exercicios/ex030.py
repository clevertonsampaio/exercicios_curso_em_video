from time import sleep
from math import trunc
num = int(input('\033[35mMe diga um numero qualquer: \033[m'))
num1 = trunc(num)
par = num1 % 2
print('\033[31mPROCESSSANDO...\033[m')
sleep(1.5)

if par == 0:
    print('O número \033[32m{}\033[m é \033[34mPAR \033[m'.format(num1))
else:
    print('O número \033[32m{}\033[m é \033[34mIMPAR \033[m'.format(num1))


