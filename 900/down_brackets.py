def solve(s):
    z=0
    for i in range(1,len(s)-1):
        if(s[i]=='('):
            z+=1
        else:
            z-=1
        if z<0:
            return "YES"
    if(z==0):
        return "NO"
    else:
        return "YES"

t = int(input())
for _ in range(t):
    s=input()
    print(solve(s))
