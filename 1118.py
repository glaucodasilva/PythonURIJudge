def lernota():
    nota = float(input())
    while nota < 0 or nota > 10:
        print('nota invalida')
        nota = float(input())
    return nota

def novocalc():
    print('novo calculo (1-sim 2-nao)')
    novo = int(input())
    if novo == 1:
        media()
    elif novo == 2:
        return
    else:
        novocalc()


def media():
    n1 = lernota()
    n2 = lernota()
    media = (n1 + n2) / 2
    print('media = %.2f' %media)
    novocalc()
    return

media()