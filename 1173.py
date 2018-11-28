n = [int(input())]
for i in range(10):
    n.append(n[i] + n[i])
for i in range(10):
    print('N[%0i] = %0i' %(i, n[i]))
