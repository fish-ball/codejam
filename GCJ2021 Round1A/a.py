import sys

sys.stdin = open('a.in')

for c in range(int(input())):
    print(f'Case #{c+1}: ', end='')
    n = int(input())
    last = 0
    ans = 0
    for x in input().split():
        if int(x) > last:
            # print(last, x)
            last = int(x)
            continue
        y = str(last)
        # print(y, x)
        i = 0
        while i < len(y) and i < len(x) and x[i] == y[i]:
            i += 1
        if i == len(y):
            x += '0'
            ans += 1
        elif i == len(x):
            while i < len(y) and y[i] == '9':
                i += 1
                x += '9'
                ans += 1
            if i == len(y):
                x += '0'
                ans += 1
            else:
                k = len(y) - len(x)
                ans += k
                x += chr(ord(y[i]) + 1) + '0' * (k - 1)
        elif x[i] < y[i]:
            k = len(y) - len(x) + 1
            ans += k
            x += '0' * k
        else:  # x[i] > y[i]
            k = len(y) - len(x)
            ans += k
            x += '0' * k
        last = int(x)
    # print(last)
    print(ans)
