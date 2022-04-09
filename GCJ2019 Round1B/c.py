#!/usr/bin/env python3
import sys

# sys.stdin = open('C-sample.in', 'r')


# sys.stdout = open('A-sample.out', 'w')

def fuck(A, N):
    A.append(9999999999)
    stack = []
    result = [0] * N
    for i in range(N + 1):
        while stack and A[i] > stack[-1][1]:
            result[stack[-1][0]] = i
            stack.pop()
        stack.append((i, A[i]))
    return result


def gao():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        NC = fuck(C, N)
        ND = fuck(D, N)
        # print(NC)
        # print(ND)
        ans = 0
        for i in range(N):
            j = i
            mc = C[i]
            md = D[i]
            while j < N:
                j0 = j
                j = min(NC[j], ND[j])
                if abs(mc - md) <= K:
                    ans += j - j0
                mc = max(C[j], mc)
                md = max(D[j], md)

        print('Case #{}: {}'.format(t + 1, ans))


if __name__ == '__main__':
    gao()
