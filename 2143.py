while True:
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        if n > 2:
            if n % 2 == 0:
                print((n-2)*2 + 2)
            else:
                print((n-1)*2 + 1)
    