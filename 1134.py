alc = 0
gas = 0
die = 0
comb = 0
while comb != 4:
    comb = int(input())
    if comb == 1:
        alc += 1
    elif comb == 2:
        gas += 1
    elif comb == 3:
        die += 1
print('MUITO OBRIGADO')
print('Alcool:', alc)
print('Gasolina:', gas)
print('Diesel:', die)

