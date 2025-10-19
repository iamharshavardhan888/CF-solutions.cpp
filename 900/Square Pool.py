for _ in range(int(input())):
    n,s=map(int,input().split())
    cnt=0

    for __ in range(n):
        i,j,x,y=map(int,input().split())

        if (x==y and i*j==1) or (x+y==s and i*j==-1):
            cnt+=1

    print(cnt)