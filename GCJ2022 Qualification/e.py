import sys
import random

for c in range(int(input())):
    n, k = map(int, input().split())
    print(f'Case #{c+1}: {n} {k}', file=sys.stderr)
    x = set(range(n)) # 剩余未探索的顶点
    s = 0
    for kk in range(k):
        r, p = map(int, input().split())
        r -= 1
        if r in x:
            x.remove(r)
        s += p
        if not x:
            break
        print('T', x.pop()+1, flush=True)
    print('E', s*n//(n-len(x))//2)
        

