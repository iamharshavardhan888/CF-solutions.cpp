for _ in range(int(input())):
    n,x,y=map(int,input().split())

    if x==y:
        print(-1)
        continue

    a=(n-1-y*n)//(x-y)
    b=n-a

    if 0<a<n and (n-1-y*n)%(x-y)==0 and (x==0 or y==0):
        if x==0:
            x,y=y,x
            a,b=b,a

        j=1

        for i in range(a):
            for __ in range(x):
                print(j,end=' ')

            if i==0:
                j+=(x+1)
            else:
                j+=x
        
        print()
    else:
        print(-1)