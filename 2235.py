cred = list(map(int, input().split()))
if cred[0] - cred[1] == 0 \
        or cred[0] - cred[2] == 0 \
        or cred[1] - cred[2] == 0 \
        or cred[0] - cred[1] + cred[2] == 0 \
        or cred[0] - cred[2] + cred[1] == 0 \
        or cred[1] - cred[0] + cred[2] == 0 \
        or cred[1] - cred[2] + cred[0] == 0 \
        or cred[2] - cred[0] + cred[1] == 0 \
        or cred[2] - cred[1] + cred[0] == 0:
    print('S')
else:
    print('N')