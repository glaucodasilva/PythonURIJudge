n = int(input())
jogadas = ['']*2
for i in range(n):
    jogadas[0] = input()
    jogadas[1] = input()
    if 'ataque' in jogadas and 'pedra' in jogadas:
        print('Jogador %d venceu' %(jogadas.index('ataque') + 1))
    elif 'papel' in jogadas and 'pedra' in jogadas:
        print('Jogador %d venceu' %(jogadas.index('pedra') + 1))
    elif 'papel' in jogadas and 'ataque' in jogadas:
        print('Jogador %d venceu' %(jogadas.index('ataque') + 1))
    elif jogadas[0] =='papel' and jogadas[1] == 'papel':
        print('Ambos venceram')
    elif jogadas[0] =='pedra' and jogadas[1] == 'pedra':
        print('Sem ganhador')
    elif jogadas[0] =='ataque' and jogadas[1] == 'ataque':
        print('Aniquilacao mutua')