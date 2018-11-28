a, b = list(map(int, input().split()))

if b < 0:
    b = b * -1
    q = (a // b) * -1
    b = b * -1
    r = a - (b * q)
else:
    q = (a // b)
    r = a - (b * q)

print(q, r)

