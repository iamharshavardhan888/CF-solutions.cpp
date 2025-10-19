for _ in range(int(input())):
    
    n=int(input())
    
    v="ae"
    s=input()
    pre=-1
    for i in range(n-2):
        chr=s[i]
        print(chr,end='')
        if chr in v:
            if s[i+1] not in v and s[i+2] not in v:
                pre=i+1
            else:
                print(".",end='')
        
        if pre==i:
            print(".",end='')
            
    print(s[-2]+s[-1])