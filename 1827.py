while True:
    try:
        n = int(input())
        matriz = []
        valor = 0
        posdois = -1
        postres = n
        posum = n//3
        for i in range(n):
            linha = []
            posdois += 1
            postres -= 1
            for j in range(n):
                valor = 0
                if j == posdois:
                    valor = 2
                if j == postres:
                    valor = 3
                if (j >= posum and j <= n - 1 - posum) and (i >= posum and i <= n - 1 - posum):
                    valor = 1
                if i == n//2 == j:
                    valor = 4
                linha.append(valor)
            matriz.append(linha)

        for i in range(n):
            linhaP = ''
            for j in range(n):
                linhaP += str(matriz[i][j])
            print(linhaP)
        print('')
    except EOFError:
        break