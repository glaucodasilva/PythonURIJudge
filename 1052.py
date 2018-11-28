mes = int(input())
if 1 <= mes <= 12:
    mes_ext = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(mes_ext[mes-1])