entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])

produtos = [0, 4, 4.5, 5, 2, 1.5]
total = quantidade * produtos[codigo]
print('Total: R$ %0.2f' % total)