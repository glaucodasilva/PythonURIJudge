oper = input()
matriz = []
soma = 0.0
ini = 0
fim = 12
cont = 0
for i in range(12):
    coluna = []
    for j in range(12):
        coluna.append(float(input()))
    matriz.append(coluna)
for k in range(5):
    ini += 1
    fim -= 1
    for y in range(ini, fim):
        cont += 1
        soma += matriz[k][y]
if oper == 'S':
    print('%.1f' %soma)
else:
    print('%.1f' %(soma/cont))