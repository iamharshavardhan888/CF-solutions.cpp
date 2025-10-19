for _ in range(1):
    nums=list(map(int,input().split()))

    nums.sort()

    a,b,c,d=nums

    if a+b>c or a+b>d or b+c>d:
        print("TRIANGLE")
    elif a+b==c or a+b==d or b+c==d:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")