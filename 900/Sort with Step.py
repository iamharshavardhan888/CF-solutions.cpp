for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    cnt=0
    for i in range(n):
        if abs(a[i]-i-1)%k!=0:
            cnt+=1
        if cnt>2:
            print(-1)
            break
    else:
        if cnt==0:
            print(0)
        else:
            print(1)