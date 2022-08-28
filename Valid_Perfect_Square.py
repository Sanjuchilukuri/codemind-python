from sys import *
t=int(input())
flag=0
while(t):
    n=int(input())
    for i in range(1,n):
        if(i*i==n):
            print("True")
            flag=1
    if(flag==0):
        print("False")
    flag=0
    t=t-1