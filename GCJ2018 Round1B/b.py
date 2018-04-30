#!/usr/bin/env python3
import sys
import random

# sys.stdin = open('b.in', 'r')


def run():
    for c in range(1, int(input()) + 1):
        x = []
        y = []
        S = int(input())
        for _ in range(S):
            d, a, b = map(int, input().strip().split())
            x.append(d + a)
            y.append(d - b)
        rx = 0
        ry = set()
        # print(*x)
        # print(*y)
        for a in set(x):
            for b in set(y):
                # print('A B:', a, b)
                mx = 0
                for i in range(S):
                    if x[i] == a or y[i] == b:
                        # print('BINGO {}'.format(i))
                        mx += 1
                        if mx > rx:
                            rx = mx
                            ry = set([i])
                        elif mx == rx:
                            ry.add(i)
                    else:
                        mx = 0

        print('Case #%d: %d %d' % (c, rx, len(ry)))


run()
