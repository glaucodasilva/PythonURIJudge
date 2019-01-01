l, c = map(int, input().split())
terreno = []
for i in range(l):
    terreno.append(list(map(int, input().split())))

if l < 3 or c < 3:
    print(0, 0)
else:
    for i in range(1,l-1):
        for j in range(2,c):
            if (terreno[i][j] == 7 and terreno[i][j-1] == 42 and terreno[i][j-2] == 7) and (terreno[i-1][j] == 7 and terreno[i-1][j - 1] == 7 and terreno[i-1][j - 2] == 7) and (terreno[i+1][j] == 7 and terreno[i+1][j - 1] == 7 and terreno[i+1][j - 2] == 7):
                print(i+1,j)
                exit()
    print(0, 0)