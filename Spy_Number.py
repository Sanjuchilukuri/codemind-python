n=int(input())
s=0
m=1
temp=n
while(n):
    r=n%10
    s+=r
    n//=10
n=temp
while(n):
    r=n%10
    m*=r
    n//=10
if(s==m):
    print("Spy Number")
else:
    print("Not Spy Number")