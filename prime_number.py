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
if(isprime(n)):
    print("prime")
else:
    print("not a prime")