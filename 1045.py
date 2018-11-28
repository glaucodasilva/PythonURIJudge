valores = input().split()
valoresOrd = sorted(map(float, valores), reverse=True)
a = valoresOrd[0]
b = valoresOrd[1]
c = valoresOrd[2]
if a > 0 and b > 0 and c > 0:
    if a >= (b+c):
        print("NAO FORMA TRIANGULO")
    else:
        if (a ** 2) == (b ** 2) + (c ** 2):
            print("TRIANGULO RETANGULO")
        if (a ** 2) > (b ** 2) + (c ** 2):
            print("TRIANGULO OBTUSANGULO")
        if (a ** 2) < (b ** 2) + (c ** 2):
            print("TRIANGULO ACUTANGULO")
        if a == b and a == c:
            print("TRIANGULO EQUILATERO")
        if (a == b or b == c or a == c) and not(a == b == c):
            print("TRIANGULO ISOSCELES")