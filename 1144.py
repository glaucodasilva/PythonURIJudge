n = int(input())
k = 0

if 1 < n < 1000:
    for col1 in range(1, n+1):
       col2 = col1 ** 2
       col3 = col1 ** 3
       print(col1, col2, col3)
       print(col1, col2+1, col3+1)

