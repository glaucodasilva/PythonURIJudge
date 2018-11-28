n = int(input())
k = 0

if 1 < n < 1000:
    for i in range(1, n+1):
        mul = i
        linha = str(i)
        for j in range(i, i + 2):
            mul *= i
            linha = linha + ' ' + str(mul)
        print(linha)
