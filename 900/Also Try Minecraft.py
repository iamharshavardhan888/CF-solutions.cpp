n,m=map(int,input().split())

hei=list(map(int,input().split()))

pre_sum=[0]

for i in range(1,n):
    fall=hei[i-1]-hei[i]
    if fall<0:
        fall=0
    
    pre_sum.append(fall+pre_sum[-1])


hei=hei[::-1]

pre_sum1=[0]

for i in range(1,n):
    fall=hei[i-1]-hei[i]
    if fall<0:
        fall=0
    
    pre_sum1.append(fall+pre_sum1[-1])




for _ in range(m):
    a,b=map(int,input().split())


    if a<b:
        print(pre_sum[b-1]-pre_sum[a-1])
    else:
        print(pre_sum1[n-b]-pre_sum1[n-a])


