def convert(val):

    aux = ''
    while val >= 100:
        if val == 900:
            rom = 'CM'
            return (rom)
        elif val == 500:
            rom = 'D' + aux
            return (rom)
        elif val == 400:
            rom = 'CD' + aux
            return (rom)
        elif val == 100:
            rom = 'C' + aux
            return (rom)
        else:
            aux = aux + 'C'
            val -= 100

    while val >= 10:
        if val == 90:
            rom = 'XC'
            return (rom)
        elif val == 50:
            rom = 'L' + aux
            return (rom)
        elif val == 40:
            rom = 'XL' + aux
            return (rom)
        elif val == 10:
            rom = 'X' + aux
            return (rom)
        else:
            aux = aux + 'X'
            val -= 10

    while val >= 1:
        if val == 9:
            rom = 'IX'
            return (rom)
        elif val == 5:
            rom = 'V' + aux
            return (rom)
        elif val == 4:
            rom = 'IV' + aux
            return (rom)
        elif val == 1:
            rom = 'I' + aux
            return (rom)
        else:
            aux = aux + 'I'
            val -= 1




dec = ('%03d' %int(input()))
romano = ''

if int(dec[0]) > 0:
    romano = convert(int(dec[0] + '00'))
if int(dec[1]) > 0:
    romano = romano + convert(int(dec[1] + '0'))
if int(dec[2]) > 0:
    romano = romano + convert(int(dec[2]))

print(romano)
