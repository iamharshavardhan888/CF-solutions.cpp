def solve():
    n,_=map(int, input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a_indices=[(a[i], i) for i in range(n)]
    a_indices.sort()
    b.sort()
    ans=[0]*n
    for i in range(n):
        ans[a_indices[i][1]]=b[i]

    print(' '.join(map(str, ans)))

t =int(input())
for _ in range(t):
    solve()
