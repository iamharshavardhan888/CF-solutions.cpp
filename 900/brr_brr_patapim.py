def missingNumber(l,n):
    actual_sum=(n*(n+1))//2
    expected_sum=0
    for i in range(1,len(l)):
        expected_sum+=l[i]
    return actual_sum-expected_sum
t=int(input())
for _ in range(t):
    n=int(input())
    grid=[]
    for i in range(n):
        temp_l=list(map(int,input().split()))
        grid.append(temp_l)
    permutation_l=[0 for i in range(2*n-1)]
    permutation_l=[-1]+permutation_l
    #Assign given permutation numbers
    for row in range(n):
        for col in range(n):
            permutation_l[row+col+1]=grid[row][col]
    #finding missing number
    permutation_l[0]=missingNumber(permutation_l,2*n)
    for number in permutation_l:
        print(number,end=" ")





