entrada = input().split()
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])
media = ((n1*2)+(n2*3)+(n3*4)+n4)/10
print('Media: %0.1f' %media)

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %0.1f' %n5)
    mediafinal = (media + n5)/2
    if mediafinal >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %0.1f' %mediafinal)