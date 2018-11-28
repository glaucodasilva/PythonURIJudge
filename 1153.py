n = int(input())
fat = n
if 1 < n < 13:
    while n > 1:
        fat = fat * (n-1)
        n -= 1
    print(fat)