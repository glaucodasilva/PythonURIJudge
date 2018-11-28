quant = int(input())
valores = list(map(int, input().split()))
teste = valores.index(min(valores))
print(teste + 1)