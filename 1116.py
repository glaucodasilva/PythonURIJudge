n = int(input())
for i in range(n):
    xy = input().split()
    if int(xy[1]) == 0:
        print('divisao impossivel')
    else:
        saida = float(xy[0])/float(xy[1])
        print("%.1f" %saida)