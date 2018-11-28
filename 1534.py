while True:
    try:
        n = int(input())

        posum = -1
        posdois = n
        matriz = []

        for i in range(n):
            coluna = []
            posum += 1
            posdois -= 1

            for j in range(n):
                if j == posum:
                    valor = 1
                if j == posdois:
                    valor = 2
                coluna.append(valor)
                valor = 3

            matriz.append(coluna)


        for i in range(n):
            linha = ''
            for j in range(n):
                linha += str(matriz[i][j])
            print(linha)

    except EOFError:
        break