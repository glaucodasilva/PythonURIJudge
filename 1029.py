def fibonacci(n):
    if n in previous.keys():
        if n not in (diccall.keys()):
            diccall[n] = 2 * diccall[n - 1] - diccall[n - 3]
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = newValue
        if n not in (diccall.keys()):
            diccall[n] = 2 * diccall[n - 1] - diccall[n - 3]
        return newValue

n = int(input())
for i in range(n):
    previous = {0: 1, 1: 1}
    diccall = {0: 0, 1: 0, 2: 2}
    val = int(input())
    fibo = fibonacci(val)
    print('fib(%d) = %d calls = %d' %(val, diccall[val], previous[val-1]))