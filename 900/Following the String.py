for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))

    alpha="abcdefghijklmnopqrstuvwxyz"

    freq={}

    for chr in alpha:
        freq[chr]=0
        
    res=""

    for i in range(n):
        num=d[i]

        for chr in freq:
            if num==freq[chr] :
                
                res+=chr
                freq[chr]+=1
                break
    
    print(res)

    




