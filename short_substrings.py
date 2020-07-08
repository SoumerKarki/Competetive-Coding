def decoder(sample):
    size=len(sample)
    i=0
    ans=''
    while i<size:
        if i==0:
            ans=ans+sample[0:2]
            i=i+3
        else:
            ans=ans+sample[i]
            i=i+2
    return ans

def main():
    t=int(input())
    b=0
    while b<t:
        sample=input()
        print(decoder(sample))
        b=b+1


main()