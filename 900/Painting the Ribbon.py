for _ in range(int(input())):
    n,m,k=map(int,input().split())

    i=n-(n+m-1)//m
    
    if i<=k:
        print("NO")
    else:
        print("YES")