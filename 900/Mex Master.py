for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    sum0=0
    f=False
    for num in l:
        if num==0:
            sum0+=1
        elif num>=2:
            f=True

    if sum0<=(n+1)//2:
        print(0) 
    elif (f or sum0==n):
        print(1)
    else:
        print(2)
