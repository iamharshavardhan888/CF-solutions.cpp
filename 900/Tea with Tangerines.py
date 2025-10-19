for _ in range(int(input())):

    n=int(input())
    nums=list(map(int,input().split()))

    op=0
    val=2*nums[0]-1


    for i in range(1,n):
        if nums[i]%val==0:

            op+=(nums[i]//val)
            op-=1
        else:

            op+=(nums[i]//val)

    print(op)
               