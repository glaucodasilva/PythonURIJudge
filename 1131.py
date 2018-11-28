def lergols():
    gols = input().split()
    inter = gols[0]
    gremio = gols[1]
    return inter, gremio

def estatistica(jogos, interV, gremioV, empate):
    inter, gremio = lergols()
    jogos += 1
    if inter > gremio:
        interV += 1
    elif gremio > inter:
        gremioV += 1
    else:
        empate += 1
    novogrenal(jogos, interV, gremioV, empate)

def novogrenal(jogos, interV, gremioV, empate):
    print('Novo grenal (1-sim 2-nao)')
    novo = int(input())
    if novo == 1:
        estatistica(jogos, interV, gremioV, empate)
    else:
        print(jogos, 'grenais')
        print('Inter:' + str(interV))
        print('Gremio:' + str(gremioV))
        print('Empates:' + str(empate))
        if interV > gremioV:
            print('Inter venceu mais')
        elif interV < gremioV:
            print('Gremio venceu mais')
        else:
            print('Nao houve vencedor')
        exit()

jogos = 0
interV = 0
gremioV = 0
empate = 0
estatistica(jogos, interV, gremioV, empate)