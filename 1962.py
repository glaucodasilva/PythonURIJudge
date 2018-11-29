n = int(input())
for i in range(n):
    ano = 2015 - int(input())
    acdc = ' D.C.'
    if ano <= 0:
        ano = (ano * (-1)) + 1
        acdc = ' A.C.'
    print(str(ano) + acdc)