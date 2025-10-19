import math
for _ in range(int(input())):
    n=int(input())

    nums=list(map(int,input().split()))

    val=math.gcd(nums[0],nums[1])

    for i in range(2,n):
        val=math.gcd(val,nums[i])

    print(nums[-1]//val)

    
