t = int(input())
for i in range(t):
    n = int(input())
    conj = {}
    for j in range(n):
        conj[j+1] = set(input().split()[1:])
    o = int(input())
    for k in range(o):
        func, conj1, conj2 = list(map(int, input().split()))
        if func == 1:
            print(len(conj[conj1].intersection(conj[conj2])))
        else:
            print(len(conj[conj1].union(conj[conj2])))