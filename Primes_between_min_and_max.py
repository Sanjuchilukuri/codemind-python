from math import *
def isprime(n):
    if(n<=1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

n = int(input())
l = list(map(int,input().split()))
maxi = l.index(max(l))
mini = l.index(min(l))
c = 0
if mini<maxi:
    for i in range(mini,maxi+1):
        if isprime(l[i]):
            c+=1
    print(c)
else:
    for i in range(maxi,mini+1):
        if isprime(l[i]):
            c+=1
    print(c)