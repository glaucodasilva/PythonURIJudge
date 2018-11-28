def fib(x):
    global call, vet, cont
    call = call + 1
    if vet[x] >= 0:
        return vet[x]
    else:
        if x == 0:
            cont[0] = 0
            vet[0] = 0
            return 0
        elif x == 1:
            cont[1] = 0
            vet[1] = 1
            return 1
        elif 1 <= x <= 39:
            cont[x] = call
            vet[x] = fib(x-1) + fib(x-2)
            return vet[x]


#PRINCIPAL
entradas = int(input())
for i in range(0,entradas):
    call = -1
    valor = int(input())
    vet = [-1] * (valor + 1)
    cont = [0] * (valor + 1)
    final = fib(valor)
    print("fib(",valor,") =",call,"calls =",final)
    print(cont)