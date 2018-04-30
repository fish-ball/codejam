#!/usr/bin/env python3
import sys

# sys.stdin = open('a.in', 'r')


def run():
    for c in range(1, int(input()) + 1):
        # print('Case {}'.format(c), file=sys.stderr)
        N, L = map(int, input().strip().split())
        result = 0
        rem = []
        R = N
        K = 100 % N
        T = N + 1 >> 1

        for a in map(int, input().strip().split()):
            result += 100 * a // N
            R -= a
            r = 100 * a % N
            # print('r = {}'.format(r))
            if r >= T:
                result += 1
            else:
                rem.append(r)
        while len(rem) < R:
            rem.append(0)
        result += R * (100 // N)
        # print(rem)
        # print('X = {}'.format(result))
        # print('R = {}'.format(R))
        # print('K = {}'.format(K))
        # print('T = {}'.format(T))
        for a in sorted(rem, reverse=True):
            if R * K + a < T:
                break
            result += 1
            R -= (T - a - 1) // K + 1

        # result += R // P if P else 0

        print('Case #%s: %d' % (c, result))


run()
