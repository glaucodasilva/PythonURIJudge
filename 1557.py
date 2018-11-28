while True:
    n = int(input())

    if n == 0:
        break

    matriz = []
    ini = 0.5
    for i in range(n):
        linha = []
        valor = int(ini * 2)
        ini = valor
        for j in range(n):
            linha.append(valor)
            valor *= 2
        matriz.append(linha)

    tam = len(str(matriz[n-1][n-1])) + 1
    for i in range(n):
        linhap = ''
        for j in range(n):
            espaco = (tam - (len(str(matriz[i][j])))) * ' '
            linhap += espaco + str(matriz[i][j])
        print(linhap[1:])
    print('')