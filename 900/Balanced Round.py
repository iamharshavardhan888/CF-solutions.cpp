for _ in range(int(input())):

    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()

    max_len=1
    _len=1

    for i in range(1,n):
        num=l[i]

        if (num-l[i-1])<=k:
            _len+=1
            max_len=max(_len,max_len)
        else:
            _len=1
    
    print(n-max_len)




