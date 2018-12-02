voo = list(map(int, input().split()))
chegada = sum(voo)
if chegada >= 24:
    chegada -= 24
elif chegada < 0:
    chegada += 24
print(chegada)