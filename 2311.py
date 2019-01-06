n = int(input())
for i in range(n):
    nome = input()
    mult = float(input())
    notas = list(map(float, input().split()))
    total = sum(notas)
    total -= max(notas)
    total -= min(notas)
    print(nome, '%.2f' % (mult*total))