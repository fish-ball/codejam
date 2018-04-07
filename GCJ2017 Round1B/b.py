#!/usr/bin/env python3
import sys

#sys.stdin = open('B-sample.in', 'r')
#sys.stdout = open('B-sample.out', 'w')

def ok(x, y):
    return (6 + x - y) % 6 not in (0,1,5)

def next(s, GG):
    A = s[2:]
    rr = []
    if not sum(A):
        return rr
    print(sorted(zip(A, range(6)))[::-1])
    for k, c in sorted(zip(A, range(6)))[::-1]:
    #for c, k in zip(range(6), A):
        if k and ok(s[1], c):
            a = list(A[:])
            a[c] -= 1
            nx = (s[0], c, *a)
            GG[(s[0], c, *a)] = tuple(s[:])
            rr.append(nx)
    return rr
    


def ko(s, GG):
    if sum(s[2:]) or not ok(s[0], s[1]): return False
    x = 'ROYGBV'[s[1]]
    while s:
        s = GG[s]
        if s:
            x = 'ROYGBV'[s[1]] + x
    return x

for z in range(1, int(input()) + 1):

    N, R, O, Y, G, B, V = map(int, input().strip().split())

    result = False

    DD = set()
    S = []
    GG = dict()

    A = [R,O,Y,G,B,V]

    #print(sorted(zip(A, range(6)))[::-1])
    for k, c in sorted(zip(A, range(6)))[::-1]:
        if not k: break
        a = A[:]
        a[c] -= 1
        #print((c,c,*a))
        XX = (c, c, *a)
        DD.add(XX)
        S.append(XX)
        GG[XX] = None
        break

    while not result and S:
        s = S.pop()
        if ko(s, GG):
            result = ko(s, GG)
            break
        for q in next(s, GG):
            if q in DD: continue
            GG[q] = s
            DD.add(q)
            S.append(q)

    print('Case #%s: %s' % (z, result or 'IMPOSSIBLE'))
