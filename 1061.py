from datetime import datetime

diainicio = input().split()
horainicio = input().split()
diafim = input().split()
horafim = input().split()

inicio = datetime(2018, 8, int(diainicio[1]), int(horainicio[0]), int(horainicio[2]), int(horainicio[4]))
fim = datetime(2018, 8, int(diafim[1]), int(horafim[0]), int(horafim[2]), int(horafim[4]))
duracao = str(fim - inicio).split()
hora = (duracao[2].split(':'))

print(duracao[0], 'dia(s)')
print(hora[0], 'hora(s)')
print(hora[1], 'minuto(s)')
print(hora[2], 'segundo(s)')