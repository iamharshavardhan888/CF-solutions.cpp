def is_blue(k):
    for paint in k:
        if paint==['R']*8:
            return True
    
    return False


for _ in range(int(input())):
    input()

    l=[]

    for i in range(8):
        temp=list(input())
        l.append(temp)

    if is_blue(l):
        print("R")
    else:
        print("B")
