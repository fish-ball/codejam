#!/usr/bin/env python3
import sys
# ferr = open('B-sample.err', 'w')
ferr = sys.stderr


T, N, M = map(int, input().strip().split())
Q = [18,17,16,14,13,11,10]
for t in range(T):
    A = []
    B = [1] * (M + 1)
    # print(B, file=ferr)
    for d in Q:
        print(*([d]*18))
        o=input()
        print(o, file=ferr)
        a = sum(map(int, o.strip().split()))
        print(a, file=ferr)
        # exit(0)
        for i in range(M+1):
            if B[i]:
                B[i] = 0 if (i-a)%d else 1
    if N > 7:
        for s in range(N-7):
            print(*([2]*18))
            input()
    print(B, file=ferr)
    for i in range(M+1):
        if B[i]:
            print(i)
            break
    input()

# ferr.close()
