x = int(input())
while x != 0:
    linha = ''
    for i in range(1, x+1):
        if i == x:
            linha = linha + str(i)
            print(linha)
        else:
            linha = linha + str(i) + ' '
    x = int(input())