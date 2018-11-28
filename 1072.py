n = int(input())
i = 1
dentro = 0
fora = 0
if n < 10000:
    while i <= n:
        x = int(input())
        if (x > (-10 ** 7)) and (x < (10 ** 7)):
            if x >= 10 and x <= 20:
                dentro = dentro + 1
            else:
                fora = fora + 1
        i = i + 1
print(dentro, "in")
print(fora, "out")