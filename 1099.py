
n = int(input())
for i in range(n):
    soma = 0
    xy = input().split()
    if int(xy[0]) > int(xy[1]):
        x = int(xy[1])
        y = int(xy[0])
    else:
        x = int(xy[0])
        y = int(xy[1])
    for j in range(x+1,y):
        if j % 2 != 0:
            soma += j
    print(soma)


