i = 1
par = 0
imp = 0
pos = 0
neg = 0
while i <= 5:
    i = i + 1
    num = int(input())
    if num % 2 == 0:
        par = par + 1
    if num > 0:
        pos = pos + 1
    if num < 0:
        neg = neg + 1
    if num % 2 != 0:
        imp = imp + 1
print(par, "valor(es) par(es)")
print(imp, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")