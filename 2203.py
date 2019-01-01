while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = list(map(float, input().split()))
        dFI = ((((xf-xi))**2)+((yf-yi)**2))**0.5
        r = r1 + r2
        if (dFI + 1.5 * vi) <= r:
            print('Y')
        else:
            print('N')
    except EOFError:
        exit()