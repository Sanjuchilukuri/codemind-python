from math import *
def isprime(n):
    if(n<=1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True

            




n=int(input())
c=0
l=0
if(isprime(n)):
    while(n):
        r=n%10
        l+=1
        if(isprime(r)):
            c+=1
        n//=10
    if(l==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
    
    
else:
    print("Not Mega Prime")
    