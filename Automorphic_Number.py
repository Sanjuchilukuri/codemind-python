n=int(input())
m=n*n
flag=0
while(n):
    r=n%10
    s=m%10
    if(r!=s):
        print("Not an Automorphic Number")
        flag=1
        break
    n//=10
    m//=10
if(flag==0):
    print("Automorphic Number")