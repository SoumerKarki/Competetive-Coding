def phy():
    a=[0,0,0]
    for i in range(int(input())):
        b=[int(x) for x in input().split()]
        a[0]=a[0]+b[0]
        a[1]=a[1]+b[1]
        a[2]=a[2]+b[2]
    if a[0]==0 and a[1]==0 and a[2]==0:
        print("YES")
    else:
        print("NO")

phy()



