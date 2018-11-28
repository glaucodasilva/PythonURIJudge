oper = input()
matriz = []
soma = 0.0
ini = 12
cont = 0
for i in range(12):
    coluna = []
    for j in range(12):
        coluna.append(float(input()))
    matriz.append(coluna)
for k in range(1, 11):
    if k <= 5:
        ini -= 1
    if k >= 7:
        ini += 1
    for y in range(ini, 12):
        cont += 1
        soma += matriz[k][y]
if oper == 'S':
    print('%.1f' %soma)
else:
    print('%.1f' %(soma/cont))