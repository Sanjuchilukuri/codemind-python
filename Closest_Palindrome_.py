def ispalin(n):
    s=str(n)
    k=s[::-1]
    return s==k
n=int(input())
i=n+1
while(True):
    if(ispalin(i)):
        a=i
        break
    i+=1
for i in range(n-1,0,-1):
    if(ispalin(i)):
        b=i
        break
d=n-b
d1=a-n
if(d>d1):
    print(a)
elif(d1>d):
    print(b)
else:
    print(b,a)