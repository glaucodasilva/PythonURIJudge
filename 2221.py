def epar(val):
    if val % 2 == 0:
        return  1
    else:
        return 0

n = int(input())
for i in range(n):
    b = int(input())
    ad, dd, ld = list(map(int, input().split()))
    ag, dg, lg = list(map(int, input().split()))
    gd = ((ad + dd) / 2) + (epar(ld) * b)
    gg = ((ag + dg)/2) + (epar(lg) * b)

    if gd > gg:
        print('Dabriel')
    elif gg > gd:
        print('Guarte')
    else:
        print('Empate')