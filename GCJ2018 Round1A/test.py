import random


def gao(L):
    done = False
    while not done:
        done = True
        for i in range(len(L) - 2):
            if L[i] > L[i + 2]:
                done = False
                L[i], L[i + 2] = L[i + 2], L[i]


def test(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True


def run():
    n = 10
    while n > 0:
        n -= 1
        L = list(range(10))
        random.shuffle(L)
        S = L[:]
        gao(L)
        if not test(L):
            print(S)
            print(L)
            print('------')


run()
