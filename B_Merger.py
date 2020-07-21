def restoreP(n,array):
    a=[]
    i=0
    for i in range(2*n):
        aux=0
        j=0
        while j<i:
            if array[j]==array[i]:
                aux=1
                break
            j=j+1
        if aux==1:
            continue
        a.append(array[i])
    i=0
    while i<n:
        print(a[i],end=' ')
        i=i+1

def main():
    t=int(input())
    r=0
    while r<t:
        n=int(input())
        sample=input().split()
        l=[int(x) for x in sample]
        restoreP(n,l)
        print()
        r=r+1

main()

