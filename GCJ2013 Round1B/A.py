from sys import stdin, stdout

#stdin = open('A-small-practice.in', 'r')
stdin = open('A-large-practice.in', 'r')
#stdout = open('A-small.out', 'w')
stdout = open('A-large.out', 'w')

T = int(stdin.readline().strip())

for t in range(0, T):

    (A, N) = [int(x) for x in stdin.readline().strip().split()]

    m = [int(x) for x in stdin.readline().strip().split()]

    ans = N

    op = 0

    m.sort()

    while A > 1 and len(m) > 0:
        while A <= m[0]:
            A += A - 1
            op += 1
        A += m[0]
        m[0:1] = []
        ans = min(ans, op + len(m))

    stdout.write('Case #{0}: {1}\n'.format(t+1, ans))

stdin.close()
stdout.close()
