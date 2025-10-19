import math
def return_pairs(l,left,right):
    correct_pairs,wrong_pairs=[0,0]
    while left<right:
        if(l[left]!=l[right]):
            wrong_pairs+=1
        else:
            correct_pairs+=1
        left+=1
        right-=1
    return [correct_pairs,wrong_pairs]
def yes_no(l,k):
    correct_pairs,wrong_pairs=return_pairs(l,0,len(l)-1)
    diff=abs(correct_pairs-k)
    

    if(correct_pairs==k):
        return "YES"
    elif(correct_pairs>k and diff<=correct_pairs and diff%2==0):
        return "YES"
    elif(correct_pairs<k and diff<=wrong_pairs and diff%2==0):
        return "YES"
    else:
        return "NO"

    
        
for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    print(yes_no(list(s),k))