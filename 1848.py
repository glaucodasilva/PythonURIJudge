caw = 0
soma = 0
dicio = {'--*': 1, '-*-': 2, '-**': 3, '*--': 4, '*-*': 5, '**-': 6, '***': 7}
while True:
    valor = input()
    if valor == 'caw caw':
        caw += 1
        print(soma)
        soma = 0
        if caw == 3:
            break
    else:
        soma += dicio[valor]