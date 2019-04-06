#!/usr/bin/env python3
import sys


# sys.stdin = open('C-sample.in', 'r')
# sys.stdout = open('C-sample.out', 'w')

def gcd(m, n):
    return gcd(n, m % n) if n else m


def gao():
    T = int(input())
    for t in range(T):
        N, L = [int(x) for x in input().strip().split()]
        A = [int(x) for x in input().strip().split()]
        D = {}
        B = [-1] * (L + 1)
        for i in range(L - 1):
            m, n = A[i:i + 2]
            if m != n:
                B[i + 1] = gcd(m, n)
        for i in range(1, L):
            if B[i] > -1 and B[i + 1] == -1:
                B[i + 1] = A[i] // B[i]
        for j in range(L - 1, 0, -1):
            if B[j] > -1 and B[j - 1] == -1:
                B[j - 1] = A[j - 1] // B[j]
        for i, x in enumerate(sorted(set(B))):
            D[x] = chr(ord('A') + i)

        print('Case #{}: {}'.format(t + 1, ''.join([D[x] for x in B])))


if __name__ == '__main__':
    gao()
