n = int(input())
dic = {'=.===': 'a', '===.=.=.=': 'b', '===.=.===.=': 'c', '===.=.=': 'd', '=': 'e', '=.=.===.=': 'f',
       '===.===.=': 'g', '=.=.=.=': 'h', '=.=': 'i', '=.===.===.===': 'j', '===.=.===': 'k', '=.===.=.=': 'l',
       '===.===': 'm', '===.=': 'n', '===.===.===': 'o', '=.===.===.=': 'p', '===.===.=.===': 'q', '=.===.=': 'r',
       '=.=.=': 's', '===': 't', '=.=.===': 'u', '=.=.=.===': 'v', '=.===.===': 'w', '===.=.=.===': 'x',
       '===.=.===.===': 'y', '===.===.=.=': 'z', '===.===.===.===.===': '0', '=.===.===.===.===': '1',
       '=.=.===.===.===': '2', '=.=.=.===.===': '3', '=.=.=.=.===': '4', '=.=.=.=.=': '5', '===.=.=.=.=': '6',
       '===.===.=.=.=': '7', '===.===.===.=.=': '8', '===.===.===.===.=': '9','=.===.=.===':'ä','=.===.===.=.===':'á',
       '===.===.===.===':'ch','=.=.===.=.=':'é','===.===.=.===.===':'ñ','===.===.===.=':'ö','=.=.===.===':'ü'}
for i in range(n):
    palavra = input().split('.......')
    resp = ''
    for j in palavra:
        codigo = j.split('...')
        if resp != '':
            resp += ' '
        for k in codigo:
            resp += dic[k]
    print(resp)

