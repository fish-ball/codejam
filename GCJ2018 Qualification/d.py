#!/usr/bin/env python3
import sys
from math import sin, cos, tan, pi, acos, asin, atan, fabs

#sys.stdin = open('D-sample.in', 'r')
# sys.stdout = open('A-sample.out', 'w')

def f1(angle):
    return sin(angle) + cos(angle)


def f2(angle):
    return sin(angle) + cos(angle) * (2 ** .5)


def run():
    for c in range(1, int(input()) + 1):
        d = float(input())
        print('d = %f' % d, file=sys.stderr)
        print('Case #%s:' % c)
        if d < 2 ** 0.5:
            # 1-dim
            l = 0
            r = pi * .25
            m = (l + r) * .5
            iterations = 64
            while iterations > 0:
                iterations -= 1
                diff = f1(m) - d
                if fabs(diff) < 1e-10:
                    break
                elif diff > 0:
                    r = m
                else:
                    l = m
                m = (l + r) * .5
                print('diff = %f' % diff, file=sys.stderr)
                print('m = %f(pi)' % m, file=sys.stderr)
            print('{:f} {:f} {:f}'.format(0, 0, 0.5))
            print('{:f} {:f} {:f}'.format(-cos(m) * .5, sin(m) * .5, 0))
            print('{:f} {:f} {:f}'.format(sin(m) * .5, cos(m) * .5, 0))

        else:
            # 2-dim
            l = 0
            r = atan(.5 * (2 ** .5))
            m = (l + r) * .5
            d45 = (2 ** .5) * .5
            iterations = 64
            while iterations:
                iterations -= 1
                diff = f2(m) - d
                if fabs(diff) < 1e-10:
                    break
                elif diff > 0:
                    r = m
                else:
                    l = m
                m = (l + r) * .5
            print('{:f} {:f} {:f}'.format(cos(m) * .5, sin(m) * .5, 0))
            print('{:f} {:f} {:f}'.format(-d45 * sin(m) * .5, d45 * cos(m) * .5, d45 * .5))
            print('{:.10f} {:.10f} {:.10f}'.format(-d45 * sin(m) * .5, d45 * cos(m) * .5, d45 * .5))


run()
