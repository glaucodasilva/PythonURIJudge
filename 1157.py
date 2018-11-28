num = int(input())
i = 1
while i <= num:
    if num % i == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1