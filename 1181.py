l = int(input())
oper = input()
matriz = []
soma = 0.0
for i in range(12):
    coluna = []
    for j in range(12):
        coluna.append(float(input()))
    matriz.append(coluna)
for k in range(12):
    soma += matriz[l][k]
if oper == 'S':
    print('%.1f' %soma)
else:
    print('%.1f' %(soma/12))