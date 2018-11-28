def ddd():
    ddd = []
    ddd.append(61)
    ddd.append('Brasilia')
    ddd.append(71)
    ddd.append('Salvador')
    ddd.append(11)
    ddd.append('Sao Paulo')
    ddd.append(21)
    ddd.append('Rio de Janeiro')
    ddd.append(32)
    ddd.append('Juiz de Fora')
    ddd.append(19)
    ddd.append('Campinas')
    ddd.append(27)
    ddd.append('Vitoria')
    ddd.append(31)
    ddd.append('Belo Horizonte')
    return ddd
def busca(ddd,valor):
    indice = 0
    while indice < len(ddd):
        if valor != ddd[indice]:
            indice = indice + 2
        else:
            return ddd[indice+1]
    return 'DDD nao cadastrado'

#PRINCIPAL
ddd = ddd()
valor = int(input())
print(busca(ddd, valor))
