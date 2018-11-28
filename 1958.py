def convert(n):
    p = n.find('.')
    if 0 < float(n) < 1:
        n = n[0] + n[2:]
        for i in range(len(n)):
            if int(n[i]) > 0:
                np = i
                break
        n = n[np] + '.' + n[np + 1:]
        numero = ('%.4f' % (float(n))) + 'E-' + str('%02d' %np)

    elif p == 1:
        numero = ('%.4f' % (float(n))) + 'E+00'
    elif p > 1:
        np = p - 1
        n = n[0] + '.' + n[1:p] + n[p + 1:]
        numero = ('%.4f' % (float(n))) + 'E+' + str('%02d' %np)
    else:
        n = n[0] + '.' + n[1:]
        np = p + len(n) - 1
        numero = ('%.4f' % (float(n))) + 'E+' + str('%02d' %np)
    return(numero)

n = input()
sinal = '+'
if n[0] == '-' or n[0] == '+':
    sinal = n[0]
    n = n[1:]
print(sinal + convert(n))



