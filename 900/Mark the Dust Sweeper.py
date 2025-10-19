for _ in range(int(input())):

    n=int(input())
    l=list(map(int,input().split()))

    ind=0
    while(ind<n and l[ind]==0):
        ind+=1
    ans=0
    for i in range(ind,n-1):
        ans+=l[i]
        if l[i]==0:
            ans+=1
            
    print(ans)
