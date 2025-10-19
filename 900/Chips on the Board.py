for _ in range(int(input())):

    n=int(input())
    b=list(map(int,input().split()))
    a=list(map(int,input().split()))

    min1=min(a)*n+sum(b)

    min2=min(b)*n+sum(a)

    print(min(min1,min2))
