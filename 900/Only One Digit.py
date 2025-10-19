for _ in range(int(input())):
    
    n=int(input())
    ans=n%10

    while n>0:
        rem=n%10
        n//=10

        ans=min(ans,rem)

    print(ans)