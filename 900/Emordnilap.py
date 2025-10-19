mod=10**9+7
N=100001
fact=[]
fact.append(1)
for i in range(1,N+1):
    fact.append(fact[-1]*i%mod)

for _ in range(int(input())):
    i=int(input())
    ans=i*(i-1)%mod

    ans=ans*fact[i]%mod

    print(ans)
    
   