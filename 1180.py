def ler():
    n = int(input())
    x = []
    lenX = n - 1
    while lenX < n:
        x.extend(input().split())
        lenX = len(x)
    return x

def menorValor(x):
    menor = int(x[0])
    pos = 0
    for i in range(1,len(x)):
        if menor > int(x[i]):
            menor = int(x[i])
            pos = i
    print('Menor valor:', menor)
    print('Posicao:', pos)
    return

#principal
x = ler()
menorValor(x)