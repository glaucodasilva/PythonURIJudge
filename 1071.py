x = int(input())
y = int(input())
y = y + 1
soma = 0
while  y < x:
    if y % 2 != 0:
        soma = soma + y
    y = y + 1
print(soma)