T = int(input())

for t in range(1, T + 1):
    N = int(input())
    k = 0
    r = 0
    c = 0
    A = []
    for i in range(N):
        row = [int(x) for x in input().strip().split(' ')]
        k += row[i]
        r += 0 if len(set(row)) == N else 1
        A.append(row)
    for col in zip(*A):
        c += 0 if len(set(col)) == N else 1
    print('Case #{}: {} {} {}'.format(t, k, r, c))
