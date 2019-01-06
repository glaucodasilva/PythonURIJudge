n = int(input())
s, b, a, s1, b1, a1 = [0]*6
for i in range(n):
    jog = input()
    v1, v2, v3 = list(map(int, input().split()))
    s += v1
    b += v2
    a += v3
    v1, v2, v3 = list(map(int, input().split()))
    s1 += v1
    b1 += v2
    a1 += v3
print('Pontos de Saque: %.2f' % (s1 * 100 / s), '%.')
print('Pontos de Bloqueio: %.2f' % (b1 * 100 / b), '%.')
print('Pontos de Ataque: %.2f' % (a1 * 100 / a), '%.')
