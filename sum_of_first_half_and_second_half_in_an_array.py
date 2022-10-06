n=int(input())
l=list(map(int,input().split()))
m=n//2
s=0
q=0
for i in range(0,m):
   s+=l[i]
for i in range(m,len(l)):
    q+=l[i]
print(s)
print(q)