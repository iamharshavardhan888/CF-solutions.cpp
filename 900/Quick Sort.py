for _ in range(int(input())):

    n,k=map(int,input().split())

    nums=list(map(int,input().split()))

    v=1

    for i in range(n):
        if nums[i]==v:
            v+=1
        
    print((n-v+k)//k)
        