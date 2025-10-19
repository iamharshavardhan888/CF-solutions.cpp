import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=abs(a[0]-1)

    for i in range(1,n):
        ans=math.gcd(ans,abs(a[i]-i-1))

    print(ans)