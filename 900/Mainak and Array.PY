for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    _min=min(l)
    _max=max(l)

    if _min==l[0] or _max==l[-1]:
        print(_max-_min)
        continue

    max_diff=max(l[-1]-_min,_max-l[0])

    
    for i in range(n):
        max_diff=max(l[i-1]-l[i],max_diff)

    print(max_diff)



    
