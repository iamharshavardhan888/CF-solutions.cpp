"""for _ in range(int(input())):
    n,m=map(int,input().split())

    nums=list(map(int,input().split()))

    freq = {}

    for val in nums:
        freq[val]=freq.get(val,0)+1
    res=[]
    for __ in range(m):

        c,l,r=input().split()
        l=int(l)
        r=int(r)

        new_freq={}
        
        for val in freq:
            
            if l<=val<=r:
                if c=="+":
                    new_freq[val+1]=new_freq.get(val+1,0)+freq.get(val)
                else:
                    new_freq[val-1]=new_freq.get(val-1,0)+freq.get(val)
            else:
                new_freq[val]=new_freq.get(val,0)+freq[val]
                
        freq=new_freq

        res.append(str(max(freq)))
        
    print(' '.join(res))""" """TIME LIMIT EXCEEDE (TLE)"""



def solve():
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    
    max_val = max(v)
    result = []
    
    for _ in range(m):
        c, l, r = input().split()
        l = int(l)
        r = int(r)
        
        if l <= max_val <= r:
            if c == '+':
                max_val += 1
            else:
                max_val -= 1
        
        result.append(str(max_val))
    
    print(' '.join(result))

# Main execution
t = int(input())
for _ in range(t):
    solve()



