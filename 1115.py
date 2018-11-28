coord = input().split()
while int(coord[0]) != 0 and int(coord[1]) != 0:
    if int(coord[0]) > 0 and int(coord[1]) > 0:
        print('primeiro')
    elif int(coord[0]) < 0 and int(coord[1]) > 0:
        print('segundo')
    elif int(coord[0]) < 0 and int(coord[1]) < 0:
        print('terceiro')
    else:
        print('quarto')
    coord = input().split()
