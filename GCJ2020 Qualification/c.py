def gao(A, result, i):
    a, b = A[i]
    for j, (c, d) in enumerate(A):
        if i == j:
            continue
        if max(b, d) - min(a, c) < b - a + d - c:
            if result[j]:
                if result[j] == result[i]:
                    return False
            else:
                result[j] = 'C' if result[i] == 'J' else 'J'
                if not gao(A, result, j):
                    return False
    return True


def main():
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        result = [''] * N
        A = []
        for i in range(N):
            A.append([int(a) for a in input().strip().split(' ')])
        for i in range(N):
            if not result[i]:
                result[i] = 'C'
                if not gao(A, result, i):
                    result = 'IMPOSSIBLE'
                    break
        print('Case #{}: {}'.format(t, ''.join(result)))


main()