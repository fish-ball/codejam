import sys

# 生成 32 bit 以内的所有素数
P = []
B = [0 for i in range(1 << 16)]

for i in range(2, 1 << 16):
    if not B[i]:
        P.append(i)
        j = i * i
        while j < (1 << 16):
            B[i] = 1
            j += i


def is_prime(number):
    for p in P:
        if p * p > number:
            return True
        if number % p == 0:
            return False
    return True


def is_good_prime(number):
    for BASE in range(2, 11):

    for b in bin(number, 2)[2:]:



sys.stdin = open('C-sample.in', 'r')
# sys.stdout = open('B-large.out', 'w')

for c in range(1, int(input()) + 1):

    N, J = map(int, input().split())

    for x in input().strip():
        if x != last:
            s += x
        last = x

    n = len(s) if s[-1] == '-' else len(s) - 1

    print('Case #%s: %s' % (c, n))
