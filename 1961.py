p, n = list(map(int, input().split()))
canos = list(map(int, input().split()))
win = True

for i in range(n-1):
    if canos[i] + p < canos[i+1]:
        print('GAME OVER')
        win = False
        break
    if canos[i] - canos[i+1] > p:
        print('GAME OVER')
        win = False
        break

if win == True:
    print('YOU WIN')