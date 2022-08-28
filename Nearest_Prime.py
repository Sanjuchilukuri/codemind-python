from math import *
def isprime(n):
    if(n==1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True



t=int(input())
while(t):
    n=int(input())
    b=0
    a=0
    for i in range(n,1,-1):
        if(isprime(i)):
            b+=i
            break
    for i in range(n,99999):
        if(isprime(i)):
            a+=i
            break
    dif=n-b
    diff=a-n
    if(dif>diff):
        print(a)
    else:
        print(b)
    t-=1
    
            