entrada = input().split()
ini = int(entrada[0])
fim = int(entrada[1])

if fim <= ini:
    fim = fim + 24
duracao = fim - ini

print('O JOGO DUROU', duracao, 'HORA(S)')