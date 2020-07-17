def oneCount(size,array):
    n=0
    count=0
    while n<size:
        if array[n]==1:
            count=count+1
        n=n+1
    return count

def modCompare(size,array):
    n=0
    count=0
    if oneCount(size,array) != (size//2):
        return -1
    while n<size-1:
        if n%2==0 and array[n]==1:
            m=n+1
            while m<size:
                if m%2==1 and array[m]==0:
                    array[n]=0
                    array[m]=1
                    count=count+1
                m=m+1
        elif n%2==1 and array[n]==0:
            m=n+1
            while m<size:
                if m%2==0 and array[m]==1:
                    array[n]=1
                    array[m]=0
                    count=count+1
                m=m+1
        n=n+1
    return count

def main():
    t=int(input())
    r=0
    while r<t:
        size=int(input())
        s=input().split()
        array=[int(x)%2 for x in s]
        print(modCompare(size,array))
        r=r+1
    return 0

main()