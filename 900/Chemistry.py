for _ in range(int(input())):
    n,k=map(int,input().split())

    s=input()

    
    op=0

    freq={}
    for chr in s:
        freq[chr]=freq.get(chr,0)+1

    for chr in freq:
        val=freq[chr]

        if val%2!=0:
            op+=1

    if op>k+1 :
        print("NO")
    else:
        print("YES")
            
    
