import sys, random

sys.stdin = open('C-large-practice.in', 'r')
sys.stdout = open('C-large.out', 'w')

for t in range(1, int(input()) + 1):
    if t == 6: break
    n = int(input())

    items = [input().strip().split() for i in range(n)]

    result = 0

    for k in range(100000):

        cnt = 0

        random.shuffle(items)
        sx = set()
        sy = set()
        for x, y in items:
            if x in sx and y in sy:
                cnt += 1
            sx.add(x)
            sy.add(y)

        result = max(result, cnt)

    print('Case #%s: %d' % (t, result))
