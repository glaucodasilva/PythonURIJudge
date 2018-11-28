n = int(input())
for i in range(n):
    c = int(input())
    soma = 1
    s = 0
    for j in range(c-1):
        if s == 0:
            soma -= 1
            s = 1
        else:
            soma += 1
            s = 0
    print(soma)
