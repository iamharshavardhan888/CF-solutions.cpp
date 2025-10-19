for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    x1,y1=list(map(int,input().split()))
    x2,y2=list(map(int,input().split()))

    poss1=[]
    poss2=[]

    def possi(a,b,x,y,p):
        
        for i in range(-a,a+1,2*a):
            for j in range(-b,b+1,2*b):
                p.append((x+i,y+j))
                if a!=b:
                    p.append((x+j,y+i))
    
    possi(a,b,x1,y1,poss1)
    possi(a,b,x2,y2,poss2)

    ans=0
    for pair in poss1:
        if pair in poss2:
            ans+=1
    
    print(ans)
    


        
