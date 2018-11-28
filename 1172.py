def ler():
    x = []
    for i in range(10):
        x.append(int(input()))
    return x

def substitui(x):
    for i in range(10):
        if x[i] <= 0:
            x[i] = 1
    return x

def imprime(xOrd):
    for i in range(len(xOrd)):
        print('X[%s] = %s' % (i, xOrd[i]))
    return
#principal
x = ler()
xOrd = substitui(x)
imprime(xOrd)