n = float(input())

if n > 0 and n < 1000000.00:
    'NOTAS'
    cem = int(n//100)
    saldo = n - (cem * 100)
    cinq = int(saldo//50)
    saldo = saldo - (cinq * 50)
    vin = int(saldo//20)
    saldo = saldo - (vin * 20)
    dez = int(saldo//10)
    saldo = saldo - (dez * 10)
    cinc = int(saldo//5)
    saldo = saldo - (cinc * 5)
    dois = int(saldo//2)
    saldo = saldo - (dois * 2)

    'MOEDAS'
    mum = int(saldo//1)
    saldo = saldo - mum
    mcinq = int(saldo//0.5)
    saldo = saldo - (mcinq * 0.5)
    mvin = int(saldo//0.25)
    saldo = saldo - (mvin * 0.25)
    mdez = int(saldo//0.10)
    saldo = saldo - (mdez * 0.10)
    mcinc = int(saldo//0.05)
    saldo = saldo - (mcinc * 0.05)
    umc = int(saldo//0.01)


    print('NOTAS:')
    print(cem,'nota(s) de R$ 100.00')
    print(cinq, 'nota(s) de R$ 50.00')
    print(vin, 'nota(s) de R$ 20.00')
    print(dez, 'nota(s) de R$ 10.00')
    print(cinc, 'nota(s) de R$ 5.00')
    print(dois, 'nota(s) de R$ 2.00')

    print('MOEDAS:')
    print(mum, 'moeda(s) de R$ 1.00')
    print(mcinq, 'moeda(s) de R$ 0.50')
    print(mvin, 'moeda(s) de R$ 0.25')
    print(mdez, 'moeda(s) de R$ 0.10')
    print(mcinc, 'moeda(s) de R$ 0.05')
    print(umc, 'moeda(s) de R$ 0.01')