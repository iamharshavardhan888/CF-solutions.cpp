for _ in range(int(input())):

    a,b,c,d=map(int,input().split())

    val1=a*d
    val2=c*b

    if ( val1 == val2 ):
        print(0)
    elif(( val1 !=0 and  val2%val1==0) or (val2!=0 and  val1%val2==0)):
        print(1)
    else:
        print(2)