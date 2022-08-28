from math import *
l=list(map(int,input().split(":")))
h=l[0]
m=l[1]
c=float((0.5)*((60*h)+m))
v=float((6*m))
b=abs(c-v)
n=min(360-b,b);
print("%.1f"%n) 