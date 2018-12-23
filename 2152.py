if __name__ == '__main__':
    ocor = int(input())
    for i in range(ocor):
        h, m, o = list(map(int, input().split()))
        if o == 0:
            print('%02d:%02d - A porta fechou!' %(h, m))
        else:
            print('%02d:%02d - A porta abriu!' %(h, m))