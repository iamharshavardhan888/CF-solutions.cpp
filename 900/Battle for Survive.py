for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    cnt=0
    for i in range(0,n-2):
        cnt+=a[i]
    
    last=a[-1]
    print(last-(a[-2]-cnt))