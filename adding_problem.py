


def increase(a,b,n):
    count=0
    while a<=n and b<=n:
        if b<=a:
            b=b+a
            count=count+1
            if b>n:
                return count
        elif b>=a:
            a=a+b
            count=count+1
            if a>n:
                return count








def main():
    t=int(input())
    r=0
    while r<t:
        s = input().split()
        (a, b, n) = (int(s[0]), int(s[1]), int(s[2]))
        print(increase(a,b,n))
        r=r+1

main()

