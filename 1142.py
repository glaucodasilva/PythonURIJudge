lin = int(input())
k = 1
for i in range(1, lin + 1):
    linha = ''
    for j in range(k, k+3):
        linha = linha + str(j) + ' '
    print(linha + 'PUM')
    k += 4
