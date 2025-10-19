for _ in range(int(input())):
    n=int(input())

    l=1
    r=3*n

    print(n//2+n%2)

    while (l<r):
        print(l,r)
        l+=3
        r-=3
    
