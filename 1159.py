n = int(input())
while n != 0:
    i = 1
    soma = 0
    while i <= 5:
        if n % 2 != 0:
            n += 1
        else:
            soma += n
            n += 2
            i += 1
    print(soma)
    n = int(input())

