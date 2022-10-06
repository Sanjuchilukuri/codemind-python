from math import *
def isprime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

c=0
n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l:
    if i>=k:
        if isprime(i):
            c+=1
print(c)