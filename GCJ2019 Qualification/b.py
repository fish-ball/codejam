#!/usr/bin/env python3
import sys

sys.stdin = open('B-sample.in', 'r')


def gao():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input().strip()
        print('Case #{}: {}'.format(t + 1, ''.join('E' if c == 'S' else 'S' for c in S)))


if __name__ == '__main__':
    gao()
