val = input().split()
x = int(val[0])
y = int(val[1])
cont = 0
linha = ''
if 1 < x < 20 and x < y < 100000:
    for i in range(1, y+1):
        cont += 1
        if cont == x:
            linha = linha + str(i)
            print(linha)
            linha = ''
            cont = 0
        else:
            linha = linha + str(i) + ' '
