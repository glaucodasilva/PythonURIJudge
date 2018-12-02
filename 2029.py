while True:
    try:
        v = float(input())
        d = float(input())
        a = 3.14 * (d/2)**2
        h = v / (3.14 * ((d/2)**2))
        print('ALTURA = %.2f' %h)
        print('AREA = %.2f' %a)
    except EOFError:
        break