cardapio = {'1001':1.50, '1002':2.50, '1003':3.50, '1004':4.50, '1005':5.50}
prod = int(input())
soma = 0
for i in range(prod):
    produto, quant = input().split()
    soma += cardapio[produto] * int(quant)
print('%.2f' %soma)