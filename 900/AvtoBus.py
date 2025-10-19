import math
for _ in range(int(input())):
    n=int(input())

    if n%2==1 or n<4:
        print(-1)
    else:
        min_bus=math.ceil(n/6.0)
        max_bus=n//4
        print(int(min_bus),max_bus)
        

