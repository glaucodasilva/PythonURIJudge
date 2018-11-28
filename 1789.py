while True:
    try:
        l = int(input())
        v = list(map(int, input().split()))
        if max(v) < 10:
            print('1')
        elif 10 <= max(v) < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break
