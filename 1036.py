valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
delta = (b**2) - (4*a*c)
if delta < 0 or a == 0 :
    print('Impossivel calcular')
else:
    r1 = (-b + (delta ** (1 / 2))) / (2 * a)
    r2 = (-b - (delta ** (1 / 2))) / (2 * a)
    print('R1 = %0.5f' % r1)
    print('R2 = %0.5f' % r2)