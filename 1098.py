i = 0
k = 3
j = 1
while i <= 2.0:
    while j <= k:
        if i == 0 or i == 1.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i, j))
        else:
            print("I=%0.1f J=%0.1f" %(i, j))
        j += 1
    i = i + 0.2
    k = k + 0.2
    j = 1 + i

