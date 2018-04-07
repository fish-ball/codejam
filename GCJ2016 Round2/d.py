import sys

sys.stdin = open('D-small-attempt2.in', 'r')
sys.stdout = open('D-small-attempt2.out', 'w')
#
# sys.stdin = open('D-sample.in', 'r')


def pre_do(g):
    n = len(g)
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if g[j][k] and g[k][l] and not g[j][l]:
                        ans += 1
                        g[j][l] = 1
    return ans


def gao():
    for t in range(1, int(input()) + 1):
        n = int(input())
        g = [list(map(int, input().strip())) for r in range(n)]

        # for i in range(n):
        #     print(''.join(map(str,g[i])))

        result = pre_do(g)

        # print('')
        # for i in range(n):
        #     print(''.join(map(str,g[i])))

        all = sum([sum(row) for row in g])

        gap1 = gap2 = 0
        for i in range(n):
            rsum = 0
            csum = 0
            for j in range(n):
                if g[i][j]:  rsum += 1
                if g[j][i]:  csum += 1
            if not rsum:
                gap1 += 1
            if not csum:
                gap2 += 1


        mm = [
            [],
            [1, 0],
            [2, 1, 0, 0, 0],
            [3, 2, 3, 6, 1, 0, 3, 0, 0, 0],
            [4, 3, -1, -1, 2, 1,-1, 9,-1, 1, 0, 0, 0, 0, 0, 0, 0],
        #    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
        ]

        # print('n', n,'all', all)

        if False:
            pass

        elif n == 2 and all == 2:
            if gap1+gap2==1:
                result += 2
        elif n == 3 and all == 2:
            if gap1+gap2==3:
                result += 3
            if gap1+gap2 == 2:
                result += 1
        elif n==3 and all==3:
            if gap1+gap2==2:
                result += 6
            if gap1+gap2==1:
                result += 2
        elif n == 4 and all == 2:
            if gap1+gap2==5:
                result += 4
            if gap1+gap2 == 4:
                result += 2

        elif n == 4 and all == 3:
            if gap1+gap2==4:
                result += 7
            if gap1+gap2 == 3:
                result += 3
            if gap1+gap2 == 2:
                result += 1

        elif n == 4 and all == 4:
            if gap1+gap2==3:
                result += 12
            if gap1+gap2 == 2:
                result += 4
            if gap1+gap2==1:
                result += 2

        elif n == 4 and all == 6:
            if gap1+gap2 == 1:
                result += 2
            if gap1+gap2 == 3:
                result += 4

        elif n == 4 and all == 8:
            if gap1 + gap2 == 2:
                result += 8

        else:
            result += mm[n][all]

        print('Case #%s: %d' % (t, result))


gao()
