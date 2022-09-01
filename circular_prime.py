from math import *
def isprime(n):
    if(n==1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True



n=int(input())
m=str(n)
m=m[::-1]
m=int(m)
if(isprime(n)):
    if(isprime(m)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    