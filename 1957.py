d = int(input())
ex = []
resp = ''

while d > 0:
    ex.append(d % 16)
    d = d // 16

ex.reverse()

for i in range(len(ex)):
    if ex[i] == 10:
        ex[i] = 'A'
    elif ex[i] == 11:
        ex[i] = 'B'
    elif ex[i] == 12:
        ex[i] = 'C'
    elif ex[i] == 13:
        ex[i] = 'D'
    elif ex[i] == 14:
        ex[i] = 'E'
    elif ex[i] == 15:
        ex[i] = 'F'

    resp = resp + str(ex[i])
print(resp)