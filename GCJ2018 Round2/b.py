#!/usr/bin/env python3
import sys
import random


# sys.stdin = open('b.in', 'r')


def gao(A, B):
    S = set()
    result = 0

    def dfs(a, b):
        nonlocal result
        for aa in range(a + 1):
            for bb in range(b + 1):
                if (aa, bb) not in S:
                    S.add((aa, bb))
                    result = max(result, len(S) - 1)
                    dfs(a - aa, b - bb)
                    S.remove((aa, bb))

    dfs(A, B)

    return result


def run():
    for c in range(1, int(input()) + 1):
        A, B = map(int, input().strip().split())

        print('Case #%d: %d' % (c, gao(A, B)))


run()
