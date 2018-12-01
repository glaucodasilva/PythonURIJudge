caso = 0
while True:
    try:
        n = int(input())
        lista = [0]
        caso += 1
        for i in range(n):
            p = i + 1
            for j in range(p):
                lista.append(p)
        if len(lista) == 1:
            print('Caso %d: %d numero' %(caso, len(lista)))
        else:
            print('Caso %d: %d numeros' % (caso, len(lista)))
        print(' '.join(map(str, lista)))
        print('')
    except EOFError:
        break