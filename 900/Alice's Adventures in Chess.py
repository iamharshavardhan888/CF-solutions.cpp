def solve(s,a,b,x,y):
    for  i in range(100):
        for char in s:
            if char=="N":
                y+=1
            elif char=="S":
                y-=1
            elif char=="W":
                x-=1
            else:
                x+=1
        
            if a==x and y==b:
                print("YES")
                return

    
    print("NO")
    
    



for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()

    x,y=[0,0]
    
    solve(s,a,b,x,y)

    