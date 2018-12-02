val = list(map(int, input().split()))

if (val[3] > val[4]) or (val[3] == 0 == val[4] and ((val[1] + val[2])%2) == (val[0]-1)*(-1)) or (val[4] > val[3]):
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')
