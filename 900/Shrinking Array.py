
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0

    for i in range(1,n):
        if abs(l[i]-l[i-1])<=1:
            flag=1
            break
    
    if flag:
        print(0)
        continue

    if flag==0 and n==2:
        print(-1)
        continue
    cnt=0
    for i in range(2,n):
        _min=min(l[i-1],l[i-2])
        _max=max(l[i-1],l[i-2])

        if _min -1 <= l[i] <= _max +1:
            cnt+=1
            break
    if n==3:
        
        if min(l[1],l[2]) -1 <= l[0] <= max(l[1],l[2]) +1:
            cnt+=1
    else:
        if (min(l[1],l[2]) -1 <= l[0] <= max(l[1],l[2]) +1) or (min(l[2],l[3]) -1 <= l[1] <= max(l[2],l[3])+1):
            cnt+=1
    
    if cnt>=1:
        print(1)
        continue

    print(-1)
    
