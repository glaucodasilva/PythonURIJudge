x = int(input())
z = int(input())
while z <= x:
    z = int(input())
soma = 0
i = x
cont = 0
while soma < z:
    soma += i
    i += 1
    cont += 1
print(cont)