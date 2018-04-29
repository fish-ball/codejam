#!/usr/bin/env python3
import sys
import random

# sys.stdin = open('B-sample.in', 'r')


# sys.stdout = open('B-sample.out', 'w')

def check(R, B, C, M, S, P, X):
    k = []
    print(X, file=sys.stderr)
    for i in range(C):
        m, s, p = M[i], S[i], P[i]
        if p > X:
            continue
        print(m, s, p, min(m, (X - p) // s), file=sys.stderr)
        pp = min(m, (X - p) // s)
        if not pp:
            continue
        k.append(min(m, (X - p) // s))
    print(k, file=sys.stderr)
    return sum(sorted(k, reverse=True)[:R]) >= B


def run():
    for c in range(1, int(input()) + 1):
        print('Case {}'.format(c), file=sys.stderr)
        R, B, C = map(int, input().strip().split())
        M = []
        S = []
        P = []
        r = 0
        for i in range(C):
            m, s, p = map(int, input().strip().split())
            M.append(m)
            S.append(s)
            P.append(p)
            r = max(r, m * s + p) + 1
        l = 0
        while r > l + 1:
            x = (r + l) // 2
            if check(R, B, C, M, S, P, x):
                r = x
            else:
                l = x

        print('Case #%s: %s' % (c, r))


run()
