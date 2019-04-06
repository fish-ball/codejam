#!/usr/bin/env python3
import sys

sys.stdin = open('c.in', 'r')


def test(G, i, x, A, path):
    print(G, i, x, A, path)
    if i in path:
        return False
    path.add(i)
    if G[i-1] >= x:
        path.remove(i)
        return True
    x -= G[i-1]
    G[i-1] = 0
    if test(G, A[i-1][0], x, A, path) and test(G, A[i-1][1], x, A, path):
        path.remove(i)
        return True
    path.remove(i)
    return False


def run():
    t = int(input())

    for c in range(t):
        M = int(input())
        A = []
        for _ in range(M):
            A.append(tuple(map(int, input().strip().split())))
        G = list(map(int, input().strip().split()))
        l = 0
        r = sum(G)
        while r > l - 1:
            m = r + l >> 1
            path = set()
            if test(list(G), 1, m, A, path):
                l = m
            else:
                r = m
        print('Case #%d: %d' % (c, l))

run()
