from math import *
n=int(input())
d=int(log10(n)+1)
temp=n
sum1=0
while(n):
    r=n%10
    sum1+=pow(r,d)
    n//=10
    d-=1
if(sum1==temp):
    print("True")
else:
    print("False")
    