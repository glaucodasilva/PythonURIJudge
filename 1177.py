t = int(input())
vet = []
prox = 0
for i in range(1000):
    vet.append(prox)
    if prox == t - 1:
        prox = 0
    else:
        prox += 1
    print('N[%d] = %d' %(i, vet[i]))
