for _ in range(int(input())):
    a,b,c=map(int,input().split())

    def ReturnVal(i,j):

        if (j-i)%2==0:
            print(1,end=' ')
        else:
            print(0,end=' ')
        

    ReturnVal(min(b,c),max(b,c))
    ReturnVal(min(a,c),max(a,c))
    ReturnVal(min(b,a),max(b,a))
    print()