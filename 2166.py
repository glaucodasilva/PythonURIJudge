n = int(input())
temp = 2.0
if n == 0:
	print('%.10f' %1)
else:
	for i in range(n-1):
		temp = 2 + 1.0/temp
	print('%0.10f' % (1+1/temp))