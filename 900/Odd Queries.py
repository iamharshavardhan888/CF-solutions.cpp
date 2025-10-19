for _ in range(int(input())):
    n,q=map(int,input().split())
    a=[0]+list(map(int,input().split()))
    
    pref=[0]
    
    for i in range(1,n+1):
        pref.append(pref[i-1]+a[i]) 
    
    for i in range(q):
        l,r,k=map(int,input().split())

        ans=pref[n]-(pref[r]-pref[l-1])+k*(r-l+1)

        if ans&1:
            print("YES")
        else:
            print("NO")



    