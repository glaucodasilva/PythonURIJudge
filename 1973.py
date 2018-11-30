n = int(input())
estrelas = list(map(int, input().split()))

soma = sum(estrelas)

i = 0
count = 0
roub = 0
while True:
    if count <= i:
        count = i + 1
    if estrelas[i] > 0:
        roub += 1
        estrelas[i] -= 1
        if (estrelas[i] + 1) % 2 != 0:
            i += 1
        else:
            i -= 1
    else:
        i -= 1
    if i == -1 or i == n:
        break
print(count, soma - roub)