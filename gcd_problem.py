
def gcd_in_list(number):
    if number == 2:
        return 1
    elif number%2==0:
        return number//2
    else:
        return (number-1)//2


def main():
    test=int(input())
    b=0
    while b<test:
        s=int(input())
        print(gcd_in_list(s))
        b=b+1

main()

