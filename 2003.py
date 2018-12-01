while True:
    try:
        hora, minuto = list(map(int, input().split(':')))
        atraso = (hora + 1) - 8
        if atraso < 0:
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: %d' %(atraso*60+minuto))
    except EOFError:
        break