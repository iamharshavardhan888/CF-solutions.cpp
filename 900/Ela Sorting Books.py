for _ in range(int(input())):
    n1,k=map(int,input().split())
    s=list(input())
    s.sort()
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
    f=[[key,freq[key]] for key in freq if freq[key]!=0]
    n=len(f)
    ans=[]
    for __ in range(k):
        freq1={}
        cnt=0
        i=0
        while cnt!=n1//k:
            i%=n
            while f[i][1]==0:
                i+=1
                i%=n
            char=f[i][0]
            freq1[char]=freq1.get(char,0)+1
            f[i][1]-=1
            cnt+=1
            i+=1

        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq1.get(char,0)==0:
                ans.append(char)
                break

    ans.sort(reverse=True)

    print(''.join(ans))


        


