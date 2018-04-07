#!/usr/bin/env python3
import sys
import random

# sys.stdin = open('B-sample.in', 'r')
# sys.stdout = open('B-sample.out', 'w')


def judge(a):
    pos = -1
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return i

    return pos


def tidy(a):
    a[0::2] = sorted(a[0::2])
    a[1::2] = sorted(a[1::2])


def calc(a):
    tidy(a)
    return judge(a)


def gao2(L):
    done = False
    while not done:
        done = True
        for i in range(len(L) - 2):
            if L[i] > L[i + 2]:
                done = False
                L[i], L[i + 2] = L[i + 2], L[i]


def test():
    n = 10
    while n > 0:
        n -= 1
        L = list(range(10))
        random.shuffle(L)
        A = L[:]
        B = L[:]
        gao2(A)
        tidy(B)

        # if judge(B) != judge(A):
        print(L)
        print(A)
        print(B)
        print('------')


# test()


def run():
    for c in range(1, int(input()) + 1):
        n = int(input())
        a = [int(x) for x in input().split()]

        pos = calc(a)

        print('Case #%s: %s' % (c, pos if pos > -1 else 'OK'))


run()
