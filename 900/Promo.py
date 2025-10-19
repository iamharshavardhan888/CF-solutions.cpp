for _ in range(1):
    n,q=map(int,input().split())

    p=list(map(int,input().split()))

    p.sort(reverse=True)
    pre_sum=[p[0]]
    for i in range(1,n):
        pre_sum.append(pre_sum[-1]+p[i])
        

    for __ in range(q):
        x,y=map(int,input().split())
        z=x-y
        
        if z==0:
            print(pre_sum[x-1])
        else:
            print(pre_sum[x-1]-pre_sum[z-1])



            


