def imprimir(vet, tipo):
    for i in range(len(vet)):
        print('%s[%d] = %d' %(tipo, i, vet[i]))
    return

par = []
impar = []
for i in range(15):
    val = int(input())
    if val % 2 == 0:
        par.append(val)
        if len(par) == 5:
            imprimir(par, 'par')
            par = []
    else:
        impar.append(val)
        if len(impar) == 5:
            imprimir(impar, 'impar')
            impar = []
imprimir(impar, 'impar')
imprimir(par, 'par')