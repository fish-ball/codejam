#!/usr/bin/env python3
import sys

sys.stdin = open('a.in', 'r')


def run():
    for c in range(1, int(input()) + 1):
        # print('Case {}'.format(c), file=sys.stderr)
        N, L = map(int, input().strip().split())


        print('Case #%s: %d' % (c, result))


run()
