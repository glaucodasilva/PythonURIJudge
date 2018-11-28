while True:
    n = int(input())
    if n == 0:
        break
    matriz = []
    inicio = 0
    restart = 1
    for i in range(n):
        coluna = []
        inicio += 1
        valor = inicio
        for j in range(n):
            if restart == 1:
                coluna.append(valor)
                valor += 1
            else:
                coluna.append(valor)
                valor -= 1
                if valor == 1:
                    restart = 1
            if j == n - 1:
                restart = 0

        matriz.append(coluna)

    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %matriz[i][j]
        print(tx[1:])
    print("")
