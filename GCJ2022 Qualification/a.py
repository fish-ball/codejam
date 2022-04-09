for n in range(int(input())):
    print(f'Case #{n+1}:')
    r, c = map(int, input().split())
    for ri in range(r):
        if not ri: 
           print('..+' + '-+'*(c-1))
        print('|' if ri else '.', end='')
        print('.|' * c)
        print('+' + '-+'*c)

