tam = int(input())
lista = list(map(int, input().split()))
t = 1

if tam != len(lista):
    t = 0
elif tam == 1:
  t = 0
elif tam == 2:
  if lista[0] != lista[1]:
    t = 1
  else:
    t = 0
else:
    if lista[0] > lista[1]:
        pos = 0
    else:
        pos = 1
    for i in range(2, tam):
        if pos:
            if lista[i] >= lista[i - 1]:
                t = 0
                break
            else:
                pos = 0
        else:
            if lista[i] <= lista[i - 1]:
                t = 0
                break
            else:
                pos = 1
print(t)