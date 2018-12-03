while True:
    notas = [100, 50, 20, 10, 5, 2]
    n, m = list(map(int, input().split()))
    troco = m - n
    if n + m == 0:
        break
    i = -1
    q = 0
    possible = False
    while q <= 2 and i <= len(notas)-2:
        i += 1
        if troco >= notas[i]:
            q += 1
            troco -= notas[i]
            i -= 1
        if troco == 0 and q == 2:
            print('possible')
            possible = True
            break
    if possible == False:
        print('impossible')
