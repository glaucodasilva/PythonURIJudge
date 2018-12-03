n = int(input())
lista = list(map(int, input().split()))
multdois = 0
multtres = 0
multquat = 0
multcinc = 0
for i in range(n):
    if lista[i] % 2 == 0:
        multdois += 1
    if lista[i] % 3 == 0:
        multtres += 1
    if lista[i] % 4 == 0:
        multquat += 1
    if lista[i] % 5 == 0:
        multcinc += 1

print('%d Multiplo(s) de 2' %multdois)
print('%d Multiplo(s) de 3' %multtres)
print('%d Multiplo(s) de 4' %multquat)
print('%d Multiplo(s) de 5' %multcinc)