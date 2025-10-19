for _ in range(int(input())):
    n,m,k=map(int,input().split())
    x,y=map(int,input().split())

    flag="YES"
    for __ in range(k):
        a,b=map(int,input().split())
        if (abs(x-a)+abs(y-b))%2==0:
            flag="NO"
            break
    
    print(flag)
    
