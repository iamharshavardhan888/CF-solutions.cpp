for _ in range(int(input())):
    r,c=map(int,input().split())
    pat=[]
    count=0
    i=0
    for k in range(r):
        row=list(input())
        pat.append(row)
        p_c=row.count('#')
        if count<p_c:
            count=p_c
            i=k

    
    row=''.join(pat[i])
    j=(row.find('#') + row.rfind('#')) // 2

    print(i+1,j+1)

        