N = int(input())
total = 0
totC = 0
totR = 0
totS = 0

for i in range(N):
    cobaia = input().split()
    total += int(cobaia[0])
    if cobaia[1] == "C":
        totC += int(cobaia[0])
    if cobaia[1] == "R":
        totR += int(cobaia[0])
    if cobaia[1] == "S":
        totS += int(cobaia[0])

print("Total:", total, "cobaias")
print("Total de coelhos:", totC)
print("Total de ratos:", totR)
print("Total de sapos:", totS)
print("Percentual de coelhos: %0.2f" %((totC * 100)/total), "%")
print("Percentual de ratos: %0.2f" %((totR * 100)/total), "%")
print("Percentual de sapos: %0.2f" %((totS * 100)/total), "%")

