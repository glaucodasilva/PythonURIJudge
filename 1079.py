N = int(input())
for i in range(N):
    valores = input().split()
    media = (((float(valores[0])*2) + (float(valores[1])*3) + (float(valores[2])*5))/10)
    print("%0.1f" %media)