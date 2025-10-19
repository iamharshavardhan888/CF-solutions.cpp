for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    cnt_pairs=0
    flag=True

    for i in range(n):
        if l[i]!=0 and flag:
            cnt_pairs+=1
            flag=False
        elif l[i]==0:
            flag=True


    if l.count(0)==n:
        print(0)
    elif cnt_pairs==1:
        print(1)
    else:
        print(2)

