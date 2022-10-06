from math import *
def isprime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
s=0
c=0
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if isprime(i):
        s+=i
        c+=1
ans=s/c
print("%.2f"%ans)