for _ in range(int(input())):

    name=input()
    n=len(name)

    if name[0:2]=="aa" or name[0:2]=="bb" or name[0:2]=="ba":
        print(name[0],name[1],name[2:])
    elif name[0:2]=="ab" and name[2:]=="b"*(n-2):
        print(name[0],name[1:n-1],name[-1])
    else:
        for i in range(2,n):
            if name[i]=='a':
                break

        print(name[0],name[1:i],name[i:])


            

            


