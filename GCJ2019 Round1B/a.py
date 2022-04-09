#!/usr/bin/env python3
import sys

# sys.stdin = open('A-sample.in', 'r')


# sys.stdout = open('A-sample.out', 'w')

def fuck(s, a, b):
    mm = dict()
    for (a0, b0), v in s.items():
        # print('fuck({}, {})'.format((a0, b0), (a, b)))
        if a > b0:
            mm[(a0, b0)] = v
        elif b < a0:
            mm[(a0, b0)] = v
        else:
            a1, b1 = max(a0, a), min(b0, b)
            if a0 < a1:
                mm[(a0, a1-1)] = v
            mm[(a1, b1)] = v + 1
            if b1 < b0:
                mm[(b1+1, b0)] = v
        # print('   ', mm)

    return mm


def gao():
    T = int(input())
    for t in range(T):
        P, Q = map(int, input().strip().split())
        sx = {(0, Q): 0}
        sy = {(0, Q): 0}
        for p in range(P):
            x, y, d = input().split()
            x = int(x)
            y = int(y)
            if d == 'E':
                sx = fuck(sx, x + 1, Q)
            elif d == 'W':
                sx = fuck(sx, 0, x - 1)
            elif d == 'N':
                sy = fuck(sy, y + 1, Q)
            elif d == 'S':
                sy = fuck(sy, 0, y - 1)
            # print(sx, sy)
        mx = 0
        xx = 0
        for (a, b), v in sx.items():
            if v > mx:
                mx = v
                xx = a
            elif v == mx:
                xx = min(xx, a)
        my = 0
        yy = 0
        for (a, b), v in sy.items():
            if v > my:
                my = v
                yy = a
            elif v == my:
                yy = min(yy, a)
        print('Case #{}: {} {}'.format(t + 1, xx, yy))


if __name__ == '__main__':
    gao()
