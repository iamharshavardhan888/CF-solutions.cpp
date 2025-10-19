for _ in range(int(input())):
    n=int(input())
    s=input()

    ans=0

    for i in range(n-2):
        if s[i]+s[i+1]+s[i+2]=='pie':
            ans+=1
        elif s[i]+s[i+1]+s[i+2]=='map':
            if i+4<=n-1 and s[i+2:i+5]!="pie":
                ans+=1
            elif i+4>n-1:
                ans+=1
    print(ans)
                