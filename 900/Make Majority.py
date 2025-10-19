for _ in range(int(input())):
    n=int(input())

    nums=list(input())

    ones=nums.count('1')
    zeros=nums.count('0')
    if ones>zeros:
        print("YES")
        continue
    else:
        paired_zeros=0
        count=0
        for i in range(n):
            num=nums[i]
            flag=int(num)
            if num=='0':
                count+=1
            elif flag==1 and count>0:
                paired_zeros+=1
            if num=="1":

                count=0
            
        if count>0:
            paired_zeros+=1
        
        if paired_zeros < ones:
            print("YES")
        else:
            print("NO")
                
