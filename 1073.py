val = int(input())
if 5 <= val <= 2000:
    for i in range(1, val+1):
        if i % 2 == 0:
            print('%d^2 = %d' %(i, i*i))