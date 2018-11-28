num = int(input())
n = num
if n > 0 and n < 1000000:
    cem = n//100
    n = n - (cem * 100)
    cin = n//50
    n = n - (cin * 50)
    vin = n//20
    n = n - (vin * 20)
    dez = n//10
    n = n - (dez * 10)
    fiv = n//5
    n = n - (cin * 5)
    duo = n//2
    one = n - (duo * 2)
    print(num)
    print(cem, "nota(s) de R$ 100,00")
    print(cin, "nota(s) de R$ 50,00")
    print(vin, "nota(s) de R$ 20,00")
    print(dez, "nota(s) de R$ 10,00")
    print(fiv, "nota(s) de R$ 5,00")
    print(duo, "nota(s) de R$ 2,00")
    print(one, "nota(s) de R$ 1,00")