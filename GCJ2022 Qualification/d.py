for c in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    p = list(map(int, input().split()))
    q = [0] * n
    ans = 0
    for i in range(n-1, -1, -1):
        j = p[i]-1
        vv = max(v[i], q[i])
        if j < 0:
            ans += vv
        elif q[j] == 0:
            q[j] = vv
        elif vv > q[j]:
            ans += vv
        elif vv <= q[j]:
            ans += q[j]
            q[j] = vv
        else:
            pass
    print(f'Case #{c+1}: {ans}')

