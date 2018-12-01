caso = 0
while True:
    try:
        n1 = input()
        tn1 = len(n1)
        n2 = input()
        caso += 1
        sub = 0
        for i in range(len(n2)):
            if n2[i:i+tn1] == n1:
                sub += 1
                pos = i + 1
        if sub > 0:
            print('Caso #%d:' %caso)
            print('Qtd.Subsequencias: %d' %sub)
            print('Pos: %d' %pos)
            print('')
        else:
            print('Caso #%d:' %caso)
            print('Nao existe subsequencia')
            print('')
    except EOFError:
        break