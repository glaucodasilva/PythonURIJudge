a = []
for i in range(100):
    numero = float(input())
    if numero // 1 == numero:
        a.append(int(numero))
    else:
        a.append(numero)
for j in range(100):
    if a[j] <= 10:
        print('A[%0i] = %.1f' %(j, a[j]))