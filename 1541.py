while True:
    valores = input()

    if valores == '0':
        break

    a, b, c = valores.split()

    areaconst = int(a) * int(b)
    terreno = areaconst * 100 / int(c)
    lado = terreno ** 0.5
    print(int(lado // 1))
