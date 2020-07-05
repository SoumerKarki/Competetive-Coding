def shorten(sample,i):
    sample=sample[:i]+sample[i+1:]
    return sample

def red_len(sample,size):
    i=size-1
    if size == 1:
        return sample
    while i>0:
        if i==size:
            i=i-1
        if sample[i]=='0' and sample[i-1]=='1':
            if i==size-1 and i-1 ==0:
                sample=shorten(sample,i-1)
                size=size-1
                return sample
            elif i==size-1 and i-1 != 0:
                sample=shorten(sample,i-1)
                size=size-1
            elif i-1==0 and i!=size-1:
                if sample[i+1]=='1':
                    sample=shorten(sample,i-1)
                    size=size-1
                elif sample[i+1]=='0':
                    sample=shorten(sample,i)
                    size=size-1
            elif i-1!=0 and i!=size-1:
                if sample[i-2]=='1' and sample[i+1]=='1':
                    sample=shorten(sample,i-1)
                    size=size-1
                elif sample[i-2]=='0' and sample[i+1]=='1':
                    sample=shorten(sample,i-1)
                    size=size-1
                elif sample[i-2]=='1' and sample[i+1]=='0':
                    sample=shorten(sample,i)
                    size=size-1
                elif sample[i-2]=='0' and sample[i+1]=='0':
                    sample=shorten(sample,i)
                    size=size-1
        else:
            i=i-1

    return sample

def main():
    t=int(input())
    b=0
    while(b<t):
        size=int(input())
        sample=input()
        print(red_len(sample,size))
        b=b+1

main()







