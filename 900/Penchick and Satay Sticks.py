t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    
    for i in range(n-1):
        if nums[i]==i+1:
            continue
        elif nums[i]==i+2 and nums[i+1]==i+1:
            nums[i],nums[i+1]=nums[i+1],nums[i]
        else:
            print("NO")
            break
    else:
        print("YES")
    
