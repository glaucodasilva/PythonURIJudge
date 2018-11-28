n = int(input())
for i in range(n):
    listjog = input().split()
    dicjog = {listjog[1] : listjog[0],listjog[3] : listjog[2] }
    n1, n2 = list(map(int, input().split()))

    if (n1 + n2) % 2 == 0:
        print(dicjog['PAR'])
    else:
        print(dicjog['IMPAR'])
