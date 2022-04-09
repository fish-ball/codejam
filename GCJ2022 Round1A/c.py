import sys

sys.stdin = open('c.in')


def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True


def solve():
    for c in range(int(input())):
        print(f'Case #{c+1}: ', end='')
        e, w = map(int, input().split())
        a = {(): 0}
        for ee in range(e):
            b = {}
            # print(f'Ex {ee+1}:')
            xx = list(map(int, input().split()))
            target = []
            for i in range(w):
                target += [i + 1] * xx[i]

            def all_perms(s):
                while True:
                    yield tuple(s)
                    if not next_permutation(s):
                        return

            for ss in all_perms(target[:]):
                minx = 999999
                for stk, step in a.items():
                    minx = min(minx, step + diff(stk, ss))
                b[ss] = minx
                # print(ss, minx)
            a = b
            # for k, v in b.items():
            # print('   ', k, v)

        print(min(v + len(k) for k, v in b.items()))


def diff(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return len(a) - i + len(b) - i


if __name__ == '__main__':
    solve()
