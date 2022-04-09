import sys
import random

for c in range(int(input())):
    n, k = map(int, input().split())
    print(f'Case #{c+1}: {n} {k}', file=sys.stderr)
    e0 = n-1
    e1 = n*(n-1)
    v = [[(0, n-1), set()] for i in range(n)]
    r0 = -1
    x = set(range(n)) # 剩余未探索的顶点
    for kk in range(k):
        r, p = map(int, input().split())
        r -= 1
        # print(r, p, f'rem={len(x)}/{k-kk}', v[r][0], file=sys.stderr)
        ee0, ee1 = v[r][0]
        if r in x:
            x.remove(r)
        v[r][0] = (p, p)
        e0 += p - ee0
        e1 += p - ee1
        if r0 > -1:
            v[r][1].add(r0)
            v[r0][1].add(r)
        xx = len(x)   
        yy = p - len(v[r0][1])
        if kk == k-1 or xx + yy <= 0:
            break
        elif True or random.randint(1, xx+yy) <= xx:
            r0 = -1
            print('T', x.pop()+1, flush=True)
        else:
            r0 = r
            print('W', flush=True)
    print('E', e0+e1>>2, flush=True)
        

