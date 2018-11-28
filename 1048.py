def calculaReajuste(salario):
    if 0 <= salario <= 400.00:
        novoSalario = salario * 1.15
        percentual = 15
    elif 400.01 <= salario <= 800.00:
        novoSalario = salario * 1.12
        percentual = 12
    elif 800.01 <= salario <= 1200.00:
        novoSalario = salario * 1.10
        percentual = 10
    elif 1200.01 <= salario <= 2000.00:
        novoSalario = salario * 1.07
        percentual = 7
    elif salario > 2000.00:
        novoSalario = salario * 1.04
        percentual = 4
    reajusteGanho = novoSalario - salario
    return saida(novoSalario, percentual,  reajusteGanho)

def saida(novoSalario, percentual,  reajusteGanho):
    print('Novo salario: %1.2f' % novoSalario)
    print('Reajuste ganho: %1.2f' % reajusteGanho)
    print('Em percentual:', percentual, '%')
    return

# Principal
salario = float(input())
calculaReajuste(salario)

