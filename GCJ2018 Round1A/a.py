#!/usr/bin/env python3
import sys
import random

# sys.stdin = open('A-sample.in', 'r')


# sys.stdout = open('B-sample.out', 'w')

def check(a, m):
    print('Check {} {}'.format(a, m), file=sys.stderr)
    n = 0
    p = [0]
    for i in range(len(a)):
        c = a[i]
        if not c:
            continue
        n += c
        if n >= m:
            if n % m:
                return False
            else:
                p.append(i + 1)
                n = 0
    return p


def run():
    for c in range(1, int(input()) + 1):
        print('Case {}'.format(c), file=sys.stderr)
        R, C, H, V = map(int, input().strip().split())
        G = [input().strip() for _ in range(R)]
        for r in G: print(r, file=sys.stderr)
        x = [0] * R
        y = [0] * C
        all = 0
        for i in range(R):
            for j in range(C):
                x[i] += 1 if G[i][j] == '@' else 0
                y[j] += 1 if G[i][j] == '@' else 0
                all += 1 if G[i][j] == '@' else 0
        yes = all % (H + 1) == 0 and all % (V + 1) == 0
        nh = all // (H + 1)
        nv = all // (V + 1)
        nn = nh // (V + 1)
        if nh % (V + 1):
            yes = False

        print(x, file=sys.stderr)
        print(y, file=sys.stderr)
        if all != 0:
            px = check(x, nh)
            py = check(y, nv)
            print(px, file=sys.stderr)
            print(py, file=sys.stderr)
            if not px or not py:
                yes = False
            else:
                for i in range(len(px) - 1):
                    x1 = px[i]
                    x2 = px[i + 1]
                    for j in range(len(py) - 1):
                        y1 = py[j]
                        y2 = py[j + 1]
                        kk = sum([sum(1 if c == '@' else 0 for c in r[y1:y2]) for r in G[x1:x2]])
                        print(kk, file=sys.stderr)
                        yes = yes and kk == nn

        print('Case #%s: %s' % (c, 'POSSIBLE' if yes else 'IMPOSSIBLE'))


run()
