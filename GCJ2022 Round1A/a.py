import sys

sys.stdin = open('a.in')

for t in range(int(input())):
    print(f'Case #{t+1}: ', end='')
    s = input()
    best = s
    acc = ''
    for i, c in enumerate(s):
        a = acc + c + c + s[i+1:]
        if a < best:
            best = a
            acc += c + c
        else:
            acc += c
    print(best)

