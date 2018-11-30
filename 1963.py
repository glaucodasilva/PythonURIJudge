a, b = list(map(float, input().split()))
percent = '%.2f' %((b * 100 / a) - 100)
print(percent + '%')