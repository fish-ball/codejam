#!/usr/bin/env python3
ferr = open('D-sample.err', 'w')


def gao():
    for t in range(int(input())):
        N, B, F = map(int, input().strip().split())
        print('N={},B={},F={}'.format(N, B, F), file=ferr)
        i = 1
        A = []
        for k in range(F):
            mask = (('0' * i + '1' * i) * (512 // i))[:N]
            print(mask)
            print('query={}'.format(mask), file=ferr)
            result = input().strip()
            print('result={}'.format(result), file=ferr)
            if result == '-1':
                exit(-1)
            A.append(result)
            i <<= 1
        print(A, file=ferr)
        # S = set(range(N)) - set(*target)
        target = [int(''.join(seq[::-1]), 2) for seq in zip(*A)]
        print('target={}'.format(target), file=ferr)
        j = 0
        S = []
        for i in range(N):
            if j < len(target) and (i & target[j]) == target[j]:
                j += 1
            else:
                S.append(i)
        print(*S)
        print(*S, file=ferr)
        result = input().strip()
        print('result={}'.format(result), file=ferr)
        if result == '-1':
            exit(-1)


if __name__ == '__main__':
    gao()
