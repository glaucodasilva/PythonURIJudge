pos = 0
soma = 0.0
for i in range(6):
    val = float(input())
    if val > 0:
        pos = pos + 1
        soma = val + soma
media = soma / pos
print(pos, 'valores positivos')
print('%0.1f' %media)