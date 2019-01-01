n = int(input())
quadras = []
for i in range(n+1):
    quadras.append(list(map(int, input().split())))

for l in range(1,n+1):
    result = ''
    for c in range(1,n+1):
        cam = quadras[l-1][c-1] + quadras[l-1][c] + quadras[l][c-1] + quadras[l][c]
        if cam >= 2:
            result += 'S'
        else:
            result += 'U'
    print(result)