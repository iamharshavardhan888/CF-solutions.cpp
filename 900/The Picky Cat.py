import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    first=abs(l[0])
    for i in range(1,n):
        if first>abs(l[i]):
            cnt+=1

    if cnt<=n//2:
        print("YES")
    else:
        print("NO")