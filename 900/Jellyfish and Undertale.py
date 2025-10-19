for _ in range(int(input())):

    a,b,n=map(int,input().split())

    l=list(map(int,input().split()))

    i=0
    ans=b-1

    for tool in l:
        b=min(1+tool,a)
        ans+=b-1



    print(ans+1)

