for _ in range(int(input())):

    n=int(input())

    if n==1:
        print(1)
    elif n&1:
        print(-1)
    else:
        p=[i for i in range(1,n+1)]

        for i in range(0,n,2):
            p[i],p[i+1]=p[i+1],p[i]

        for num in p:
            print(num,end=' ')

    
