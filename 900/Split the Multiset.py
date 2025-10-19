for _ in range(int(input())):
    n,k=map(int,input().split())
    
    ans=0

    while(n>1):
        n-=(k-1)
        ans+=1
    print(ans)