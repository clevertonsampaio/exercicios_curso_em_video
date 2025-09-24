s = 0
con = 0
for c in range(1, 501, 2):
    d = c % 3
    if d == 0:
        s += c
        con = con + 1
print('A soma de todos os {} valores solicitados é {} '.format(con, s))
