maior = 0
for i in range(1,101):
    val = int(input())
    if maior < val:
        maior = val
        pos = i
print(maior)
print(pos)
