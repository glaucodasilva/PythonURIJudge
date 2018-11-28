n = int(input())
for i in range(n):
    p = int(input())
    for j in range(2, p + 1):
        if p == j:
            print(p, 'eh primo')
            break
        elif p % j == 0:
            print(p, 'nao eh primo')
            break