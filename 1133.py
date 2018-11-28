val1 = int(input())
val2 = int(input())
if val1 > val2:
    ini = val2
    fim = val1
else:
    ini = val1
    fim = val2
for i in range(ini + 1, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)