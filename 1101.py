def ler():
    xy = input().split()
    if int(xy[0]) > int(xy[1]):
        x = int(xy[1])
        y = int(xy[0])
    else:
        x = int(xy[0])
        y = int(xy[1])
    return x,y

x, y = ler()
while x > 0 and y > 0:
    soma = 0
    sequencia = ''
    for j in range(x, y+1):
        soma += j
        sequencia = sequencia + str(j) + ' '
    print(sequencia + 'Sum=' + str(soma))
    x, y = ler()




