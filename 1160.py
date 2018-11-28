t = int(input())
for i in range(t):
    caso = input().split()
    pa = int(caso[0])
    pb = int(caso[1])
    g1 = float(caso[2])
    g2 = float(caso[3])
    anos = 0
    while pa <= pb:
        p1 = int(pa * (g1 / 100))
        p2 = int(pb * (g2 / 100))
        pa += p1
        pb += p2
        anos += 1
        if anos > 100:
            break

    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(anos, 'anos.')