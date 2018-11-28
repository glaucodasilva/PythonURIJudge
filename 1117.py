def lernota():
    nota = float(input())
    while nota < 0 or nota > 10:
        print('nota invalida')
        nota = float(input())
    return nota

n1 = lernota()
n2 = lernota()
media = (n1 + n2) / 2
print('media = %.2f' %media)