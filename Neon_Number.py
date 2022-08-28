from math import *
n=int(input())
su=n**2
sum1=0
while(su):
    sum1=sum1+su%10
    su=su//10
    
if(sum1==n):
    print("Neon Number")
else:
    print("Not Neon Number")