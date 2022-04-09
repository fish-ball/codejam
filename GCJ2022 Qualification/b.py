for n in range(int(input())):
    print(f'Case #{n+1}: ', end='')
    g = [list(map(int, input().split())) for i in range(3)]
    d = []
    rem = 1000000
    for x in zip(*g):
        p = min(rem, min(x))
        d.append(p)
        rem -= p
    if rem > 0:
        print('IMPOSSIBLE')
    else:
        print(' '.join(map(str, d)))
        

