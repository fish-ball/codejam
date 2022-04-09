for c in range(int(input())):
    print(f'Case #{c+1}: ', end='')
    n = int(input())
    k = 0
    ans = 0
    for i, x in enumerate(sorted(map(int, input().split()))):
        k = min(k+1, x)
        ans = max(ans, k)
    print(ans)
