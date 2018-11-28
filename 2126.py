def comparaValores(n1, n2, caso):
    qtd = 0
    caso = caso + 1
    fim = len(n1)
    i = 0
    while i <= (len(n2)-(len(n1) - 1)):
        compara = n2[i:fim]
        if n1 == compara:
            qtd = qtd + 1
            pos = i + 1
            i = fim
            fim = i + len(n1)
        elif (i + len(n1) >= len(n2)) and qtd == 0:
            i = i + len(n1)
            print()
            print('Caso #%s' % caso)
            print('Nao existe subsequencia')
        else:
            i = i + 1
            fim = i + len(n1)

    if qtd > 0:
        print()
        print('Caso #%s' % caso)
        print('Qtd.Subsequencias:', qtd)
        print('Pos:', pos)
    return caso

#Principal
n1 = input()
n2 = input()
caso = 0
while True:
    try:
        while (1 < int(n1) < 10 ** 10) and (int(n1) < int(n2) < 10 ** 32):
            caso = comparaValores(n1, n2, caso)
            n1 = input()
            n2 = input()
    except:
        break