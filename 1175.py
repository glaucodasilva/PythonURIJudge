n = 20 * [0]
i = 19
while i >= 0:
    n[i] = int(input())
    i -= 1
for j in range(20):
    print('N[%0i] = %0i' %(j, n[j]))