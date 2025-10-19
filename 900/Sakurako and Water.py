"""

t=int(input())
for _ in range(t):
    n=int(input())
    height=[]
    indices=[]
    for i in range(n):
        height.append(list(map(int,input().split())))
        for j in range(n):
            if height[i][j]<0:
                indices.append([i,j])

    min_magic=0

    for k in range(0,n):
        temp=[]
        for pair in indices:
            if pair[0]-pair[1]==k and pair[0]>=pair[1]:
                temp.append(-height[pair[0]][pair[1]])
        if len(temp)>0:
            min_magic+=max(temp)
    

    for k in range(1,n):
        temp=[]
        for pair in indices:
            if -pair[0]+pair[1]==k and pair[0]<pair[1]:
                temp.append(-height[pair[0]][pair[1]])
        if len(temp)>0:
            min_magic+=max(temp)
 

    print(min_magic)

"""
def solve():
    n = int(input())
    mn = dict()
    for i in range(n):
        a = [int(x) for x in input().split()]
        for j in range(n):
            mn[i - j] = min(a[j], mn.get(i - j, 0))
    ans = 0
    for value in mn.values():
        ans -= value
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()

