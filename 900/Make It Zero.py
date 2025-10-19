t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    if (n&1):
        print("4")
        print("1 "+str(n-1))
        print("1 "+str(n-1))
        print(str(n-1)+" "+str(n))
        print(str(n-1)+" "+str(n))

    else:
        print("2")
        print("1 "+str(n))
        print("1 "+str(n))



    