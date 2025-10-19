import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    

    ans=0

    for i in range(n-2,-1,-1):
        while l[i]>=l[i+1] and l[i]>0:
            l[i]//=2
            ans+=1
        
        if l[i]==l[i+1]:
            print(-1)
            break
    else:
        print(ans)
        