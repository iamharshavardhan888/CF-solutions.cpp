for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    
    bad=n//2-k
    k1=s.count('0')
    k2=s.count('1')
    
    if k1>=bad and k2>=bad:
        k1-=bad
        k2-=bad
        if k1%2==0 and k2%2==0:
            print("YES")
            continue
    
    print("NO")