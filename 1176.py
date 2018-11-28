a = 0
b = 1
fib = [0, 1]
for i in range(60):
    prox = a + b
    a = b
    b = prox
    fib.append(prox)

n = int(input())
for j in range(n):
    t = int(input())
    print('Fib(%d) = %d' %(t, fib[t]))