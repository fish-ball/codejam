#!/usr/bin/env python3
import sys

sys.stdin = open('A-sample.in', 'r')
# sys.stdout = open('A-sample.out', 'w')

B = []
path = []
R = 0
C = 0
DX = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1]
DY = [2, -2, -2, 2, 3, -3, -3, 3, 4, -4, -4, 4]
#DX = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 2, 2, -2, -2]
#DY = [2, -2, -2, 2, 3, -3, -3, 3, 4, -4, -4, 4, 3, -3, -3, 3]
[DX, DY] = [DX + DY, DY + DX]
D = len(DX)


def search(x, y, rem):
    global R, C, B, path, DX, DY
    i = x*C+y
    B[i] = 1
    path.append((x, y))
    if not rem:
        return True
    for dx, dy in zip(DX, DY):
        x += dx
        y += dy
        if 0 <= x < R and 0 <= y < C and not B[x*C+y]:
            if search(x, y, rem-1):
                return True
        x -= dx
        y -= dy
    B[i] = 0
    path.pop()
    return False


def gao():
    T = int(input())
    global R, C, B, path, DX, DY
    for t in range(T):
        R, C = map(int, input().split())
        swap = 0
        # print(R, C, file=sys.stdout)
        if R > C:
            swap = 1
            C, R = R, C
        B = [0] * (R * C)
        path = []
        result = search(0, 0, R*C-1) \
            or search(0, 1, R*C-1)
            # or search(1, 1, R*C-1) \
            # or C>=7 and search(0, 2, R*C-1) \
            # or C>=9 and search(0, 3, R*C-1)
        print('Case #{}: {}'.format(t + 1, 'POSSIBLE' if result else 'IMPOSSIBLE'))
        if result:
            for x, y in path:
                if swap:
                    print(y+1, x+1)
                else:
                    print(x+1, y+1)


if __name__ == '__main__':
    gao()
