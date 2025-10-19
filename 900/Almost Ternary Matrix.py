for _ in range(int(input())):
    n,m=map(int,input().split())
    ele1="0 1 "
    ele2="1 0 "
    row1=""
    row2=""

    for i in range(m//2):
        row1+=[ele1,ele2][i&1]
        row2+=[ele2,ele1][i&1]

    

    pos1=row1+"\n"+row2
    pos2=row2+"\n"+row1
    

    for j in range(n//2):
        print([pos1,pos2][j&1])





    

    