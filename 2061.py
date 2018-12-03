abas, acoes = list(map(int, input().split()))
for i in range(acoes):
    if input() == 'fechou':
        abas += 1
    else:
        abas -= 1
print(abas)