from sys import stderr

for t in range(int(input())):
    n = int(input())
    # print(f'Case #{t+1}: ', end='')
    a = []
    for i in range(n):
        if (1 << i) >= 10 ** 9:
            break
        a.append(1 << i)
    aa = [256 + i + 1 for i in range(n - len(a))]
    # print(*a, file=stderr)
    # print(*aa, file=stderr)
    print(*a, *aa)
    b = list(map(int, input().split())) + aa
    summary = sum(a) + sum(b)
    left = []
    right = []
    rem = 0
    for bb in b:
        if 0 <= rem + bb < a[-1] * 2:
            left.append(bb)
            rem += bb
        elif 0 <= rem - bb < a[-1] * 2:
            right.append(bb)
            rem -= bb
        elif 0 <= bb - rem < a[-1] * 2:
            right.append(bb)
            rem = bb - rem
            left, right = right, left
        else:
            raise Exception('malformed data')
    print(f'rem = {rem}', file=stderr)
    # print(left, file=stderr)
    # print(right, file=stderr)
    total = sum(a) + rem
    target = total // 2
    left1 = []
    right1 = []
    for i, x in enumerate(a):
        if (1 << i) & target:
            left1.append(x)
        else:
            right1.append(x)
    # print(sum(left) - sum(right), rem, file=stderr)
    # print(sum(left) + sum(right), sum(b), file=stderr)
    # print(sum(left1), sum(right1) + rem, target, file=stderr)
    # print(sum(left1) + sum(right), summary // 2, file=stderr)

    # print(f'total = {total}, target = {total//2}', file=stderr)

    print(*(left1 + right))
