T = int(input())

for t in range(1, T + 1):
    A = input().strip()
    d = 0
    a = ''
    for c in A:
        dd = int(c)
        while dd > d:
            d += 1
            a += '('
        while dd < d:
            d -= 1
            a += ')'
        a += c
    while d > 0:
        d -= 1
        a += ')'
    print('Case #{}: {}'.format(t, a))
