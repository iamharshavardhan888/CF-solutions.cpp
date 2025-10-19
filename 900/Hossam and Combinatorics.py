for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    _min=float('+inf')
    _max=float('-inf')

    for num in nums:
        if _min>num:
            _min=num
            cnt_min=1
        elif _min==num:
            cnt_min+=1

        if _max<num:
            _max=num
            cnt_max=1
        elif _max==num:
            cnt_max+=1

    if _min==_max:
        print(n*(n-1))
    else:
        print(2*cnt_max*cnt_min)

