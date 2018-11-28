n = int(input())
for i in range(n):
    val = input().split()
    ini = int(val[0])
    fim = int(val[1])
    i = 1
    soma = 0
    while i <= fim:
        if ini % 2 == 0:
            ini += 1
        else:
            soma += ini
            ini += 2
            i += 1
    print(soma)
