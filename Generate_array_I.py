n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,n,2):
    for j in range(0,a[i+1]):
        c.append(a[i])
print(*c)