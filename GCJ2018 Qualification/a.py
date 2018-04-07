#!/usr/bin/env python3
import sys

sys.stdin = open('A-sample.in', 'r')
sys.stdout = open('A-sample.out', 'w')


def next_seq(seq):
    for i in range(1, len(seq)):
        if seq[i - 1] == 'S' and seq[i] == 'C':
            return seq[0:i - 1] + seq[i] + seq[i - 1] + seq[i + 1:]
    return False


def eval_seq(seq):
    dam = 1
    effect = 0
    for action in seq[::-1]:
        if action == 'S':
            effect += dam
        elif action == 'C':
            dam *= 2
        else:
            raise Exception('OMG')
    return effect


for c in range(1, int(input()) + 1):
    d, p = input().strip().split(' ')
    d = int(d)

    n = 0
    p = p[::-1]
    while d < eval_seq(p):
        p = next_seq(p)
        if p:
            n += 1
        else:
            n = -1
            break

    print('Case #%s: %s' % (c, n if n >= 0 else 'IMPOSSIBLE'))
