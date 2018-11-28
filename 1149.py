val = input().split()
soma = 0
a = int(val[0])
n = int(val[len(val)-1])
for i in range(n):
    soma = soma + a + i
print(soma)
