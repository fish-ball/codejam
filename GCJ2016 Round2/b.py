import sys

sys.stdin = open('B-small-attempt0.in', 'r')


sys.stdout = open('B-small-attempt0.out', 'w')


def solve(A):
    # print('A', A)

    N = len(A)
    L = [1]
    for i in range(N):
        p = A[i]
        X = [0] * (i + 2)
        # j = i
        # while j >= 0:
        #     L[j + 1] += L[j] * p
        #     L[j] += L[j] * (1 - p)
        #     j -= 1
        for j in range(i + 1):
            X[j + 1] += L[j] * p
            X[j] += L[j] * (1 - p)
        L = X
    return L[N // 2]


def gao():
    for t in range(1, int(input()) + 1):

        _N, K = map(int, input().split())
        P = sorted(map(float, input().split()))

        result = 0

        for b in range(2 ** _N):
            # print(bin(b))
            if sum([1 for c in bin(b) if c == '1']) != K:
                continue
            result = max(result, solve([P[p] for p in range(_N) if (1 << p) & b]))

        print('Case #%s: %.6f' % (t, result))


gao()
