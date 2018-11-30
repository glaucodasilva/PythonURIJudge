alunos = int(input())
escolhido = 'Minimum note not reached'
maior = 8.0
for i in range(alunos):
    aluno = input().split()
    if float(aluno[1]) >= maior:
        escolhido = aluno[0]
        maior = float(aluno[1])
print(escolhido)