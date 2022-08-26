def ispalin(n):
    s=str(n)
    k=s[::-1]
    if(s==k):
        return True
    else:
        return False




n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    if(ispalin(i)):
        l.append(i)
print(*l)