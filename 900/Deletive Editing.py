for _ in range(int(input())):
    s1,s2=map(str,input().split())
    n,m=len(s1)-1,len(s2)-1
    freq={}
    s1=list(s1)

    for char in s2:
        freq[char]=freq.get(char,0)+1

    for i in range(n,-1,-1):
        if freq.get(s1[i],0)!=0:
            freq[s1[i]]-=1
        else:
            s1[i]='.'

    res=""

    for char in s1:
        if char!='.':
            res+=char

    if res==s2:
        print("YES")
    else:
        print("NO")

