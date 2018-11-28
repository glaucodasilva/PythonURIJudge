val1 = int(input())
val2 = int(input())
soma = 0
if val1 > val2:
    ini = val2
    fim = val1
else:
    ini = val1
    fim = val2
for i in range(ini, fim+1):
    if i % 13 != 0:
        soma += i
print(soma)