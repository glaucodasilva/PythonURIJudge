from datetime import datetime
while True:
    try:
        mes, dia = input().split()
        natal = datetime.strptime(('25/12/2016'), "%d/%m/%Y").date()
        data = datetime.strptime((dia + '/' + mes + '/2016'), "%d/%m/%Y").date()
        faltam = str(natal - data).split()[0]
        if faltam == '0:00:00':
            print('E natal!')
        elif int(faltam) == 1:
            print('E vespera de natal!')
        elif int(faltam) < 0:
            print('Ja passou!')
        else:
            print('Faltam %d dias para o natal!' %(int(faltam)))
    except EOFError:
        break