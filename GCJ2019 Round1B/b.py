#!/usr/bin/env python3
import sys

ferr = open('B-sample.err', 'w')
# ferr = sys.stderr

M = 1 << 63


def test(r1, r2, r3, r4, r5, r6, a):
    x = (r1 * (1 << 62)
         + r2 * (1 << 31)
         + r3 * (1 << 20)
         + r4 * (1 << 15)
         + r5 * (1 << 12)
         + r6 * (1 << 10)) % M
    print("test", r1, r2, r3, r4, r5, r6, x, a, file=ferr)
    return x == a


def gao():
    T, W = map(int, input().strip().split())
    for t in range(T):
        Q = [1, 62, 1, 1, 1, 1][:W]
        A = []
        for q in Q:
            print(q)
            A.append(int(input()))
        a1 = A[0]
        a62 = A[1]
        print(A, file=ferr)
        ans = None
        rem = a1 + 1
        r2 = (a62 >> 31) % 128
        r3 = (a62 >> 20) % 128
        for r1 in range(rem):
            rem -= r1
            rem -= r2
            rem -= r3
            for r4 in range(rem):
                rem -= r4
                for r5 in range(rem):
                    rem -= r5
                    if test(r1, r2, r3, r4, r5, rem, a62):
                        ans = [r1, r2, r3, r4, r5, rem]
                    if ans: break
                    rem += r5
                if ans: break
                rem += r4
            rem += r3
            rem += r2
            if ans: break
            rem += r1 + r1
        print(*ans)
        print(*ans, file=ferr)
        result = input().strip()
        print(result, file=ferr)
        if result == '-1':
            exit(1)


gao()
# ferr.close()
