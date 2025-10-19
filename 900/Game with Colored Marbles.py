t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    freq=dict()

    for i in nums:
        freq[i]=freq.get(i,0)+1
    
    

    l=[(key,freq[key]) for key in freq]
    
    if len(freq)!=n:
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i][1]>l[j][1]:
                    l[i],l[j]=l[j],l[i]
    

    temp=[]

    for x in l:
        for _ in range(x[1]):
            temp.append(x[0])

    nums=temp.copy()

    alice=0
    bob=n-1

    alice_freq=dict()
    while alice<=bob:
        alice_freq[nums[alice]]=alice_freq.get(nums[alice],0)+1
        alice+=1
        bob-=1
    

    score=0
    for key in alice_freq:
        if alice_freq[key]==freq[key]:
            score+=2
        else:
            score+=1
    
    print(score)




