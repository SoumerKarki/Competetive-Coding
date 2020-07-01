
def stend(sample,i):
    sample=sample[:i]+sample[i+1:]+sample[i]
    return sample

def bprob3(sample,size):
    i=0
    lb=0
    rb=0
    d=0
    count=0
    while i<size:
        if sample[i]=='(':
            lb=lb+1
            d=lb-rb
            i=i+1
        elif sample[i]==')':
            rb=rb+1
            d=lb-rb
            if d==0:
                lb=0
                rb=0
                i=i+1
            elif d<0:
                sample=stend(sample,i)
                lb=0
                rb=0
                count=count+1
            elif d>0:
                i=i+1
    return count










def main():
    t=int(input())
    b=0
    while b<t:
        size=int(input())
        sample=input()
        print(bprob3(sample,size))
        b=b+1

main()
