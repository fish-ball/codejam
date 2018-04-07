#!/usr/bin/env python3
import sys

#sys.stdin = open('B-sample.in', 'r')
#sys.stdout = open('B-sample.out', 'w')

def ok(x, y):
    return (6 + x - y) % 6 not in (0,1,5)

for z in range(1, int(input()) + 1):

    N, R, O, Y, G, B, V = map(int, input().strip().split())

    S = set()
    GG = dict()
    A = [R,O,Y,G,B,V]
    for c, k in zip(range(6), A):
        if not k: continue
        a = A[:]
        a[c] -= 1
        #print((c,c,*a))
        S.add((c, c, *a))
        GG[(c, c, *a)] = None

    #for xx in S: print(xx)

    for i in range(1, N):
        #print('>>> Round %d' % i)
        Q = set()
        for s in S:
            A = s[2:]
            for c, k in zip(range(6), A):
                if k and ok(s[1], c):
                    a = list(A[:])
                    a[c] -= 1
                    Q.add((s[0], c, *a))
                    GG[(s[0], c, *a)] = tuple(s[:])
        S = Q
        #for xx in S: print(xx)

    result = False
    for s in S:
        if ok(s[0], s[1]):
            result = 'ROYGBV'[s[1]]
            while s:
                s = GG[s]
                if s:
                    result = 'ROYGBV'[s[1]] + result
            break

    print('Case #%s: %s' % (z, result or 'IMPOSSIBLE'))
