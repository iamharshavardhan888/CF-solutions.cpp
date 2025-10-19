for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))


    ans=0
    for num in l:
        ans+=(2*num-1)

    print(ans-(2*max(l)-1))