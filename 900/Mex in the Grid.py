for _ in range(int(input())):
    n=int(input())

    l=[[0 for __ in range(n)] for j in range(n)]
    top,bottom,left,right=0,n-1,0,n-1
    val=n*n-1
    while top<bottom:
        for j in range(left,right+1):
            l[bottom][j]=val
            val-=1
        for i in range(bottom-1,top,-1):
            l[i][right]=val
            val-=1
        for j in range(right,left-1,-1):
            l[top][j]=val
            val-=1
        for i in range(top+1,bottom):
            l[i][left]=val
            val-=1

        top+=1
        bottom-=1
        left+=1
        right-=1

    for i in range(n):
        for j in range(n):
            print(l[i][j],end=' ')
        print()
        