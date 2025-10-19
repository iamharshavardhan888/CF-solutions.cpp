for _ in range(int(input())):

    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    _max=float('-inf')
    _min=float('+inf')    
    _sum=0
    for gap in a:
        _sum+=gap
        _max=max(_max,gap)
        _min=min(_min,gap)

    if n+_sum+_max-_min<=m:
        print("YES")
    else:
        print("NO")



