retas = list(map(int, input().split())).sort()
retas.sort()
if sum(retas) - retas[2] > retas[2]:
    if retas[0] == retas[1] == retas[2]:
        print('Valido-Equilatero')
    elif retas[0] != retas[1] != retas[2]:
        print('Valido-Escaleno')
    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
        print('Valido-Isoceles')
    if retas[2]**2 == retas[1]**2 + retas[0]**2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Invalido')