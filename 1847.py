a, b, c = list(map(int, input().split()))

cb = c - b
ba = b - a
if cb > ba:
    print(':)')
elif ba > cb:
    print(':(')
elif cb > 0:
    print(':)')
else:
    print(':(')
