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
flag=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i*j==n):
            if(isprime(i) and isprime(j)):
                print(i,j)
                flag=1
                break
    if(flag==1):
        break
if(flag==0):
    print(-1)