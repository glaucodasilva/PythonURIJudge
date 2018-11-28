def maior4500(salariobase):
    imposto = ((salariobase - 4500.00) * 0.28)
    salariobase = 4500.00
    return(maior3000(salariobase, imposto))

def maior3000(salariobase, imposto):
    imposto = ((salariobase - 3000.00) * 0.18) + imposto
    salariobase = 3000.00
    return(maior2000(salariobase,imposto))

def maior2000(salariobase, imposto):
    imposto = ((salariobase - 2000.00) * 0.08) + imposto
    return(imposto)


salario = float(input())

if salario > 4500.00:
    print('R$ %0.2f' %maior4500(salario))
elif salario > 3000.00:
    print('R$ %0.2f' %maior3000(salario, 0.0))
elif salario > 2000.00:
    print('R$ %0.2f' %maior2000(salario, 0.0))
else:
    print('Isento')

