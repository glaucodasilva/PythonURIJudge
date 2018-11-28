n = int(input())
a = 0
b = 1
prox = 0
fib = '0 1'
if 1 < n < 46:
    for i in range(1, n-1):
        prox = a + b
        a = b
        b = prox
        fib = fib + ' ' + str(prox)
    print(fib)
