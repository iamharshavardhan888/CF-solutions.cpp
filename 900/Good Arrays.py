for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    _sum=0
    cnt_1=0

    for num in l:
        _sum+=num
        if num==1:
            cnt_1+=1

    if _sum>=cnt_1+n and n>1:
        print("YES")
    else:
        print("NO")