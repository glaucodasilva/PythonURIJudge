idade = int(input())
soma = 0
cont = 0
while idade > 0:
    soma += idade
    cont += 1
    idade = int(input())
print('%.2f' %(soma/cont))