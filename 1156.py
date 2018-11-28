s = 1
k = 2
for i in range(3, 39+1, 2):
    s = s + (i/k)
    k = k + k
print('%.2f' %s)