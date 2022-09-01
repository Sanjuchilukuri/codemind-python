from math import *
n=int(input())
flag=0
sq=int(sqrt(n))
for i in range(1,sq+1):
    if(i*(i+1)==n):
        print("YES")
        flag=1
        break
if(flag==0):
    print("NO")
    