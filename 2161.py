n = int(input())
temp = 6.0
if n == 0:
	print('%.10f' %3)
else:
	for i in range(n-1):
		temp = 6 + 1.0/temp
	print('%0.10f' % (3+1/temp))