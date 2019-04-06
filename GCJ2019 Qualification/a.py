#!/usr/bin/env python3
import sys

sys.stdin = open('A-sample.in', 'r')


# sys.stdout = open('A-sample.out', 'w')


def gao():
    T = int(input())
    for t in range(T):
        N = int(input())
        X = 0
        for i, c in enumerate(str(N)):
            X *= 10
            if c == '4':
                X += 1
        print('Case #{}: {} {}'.format(t + 1, X, N - X))


if __name__ == '__main__':
    gao()
