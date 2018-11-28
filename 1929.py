val = list(map(int, input().split()))
val.sort()
a, b, c, d = val

if a + b > c:
    print('S')
elif b + c > d:
    print('S')
else:
    print('N')