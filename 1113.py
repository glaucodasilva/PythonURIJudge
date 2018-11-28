xy = input().split()
while int(xy[0]) != int(xy[1]):
    if int(xy[0]) > int(xy[1]):
        print("Decrescente")
    else:
        print("Crescente")
    xy = input().split()
