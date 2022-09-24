n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
d=[]
for i in range(0,n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        d.append(a[i])
if len(d)==0:
    print('-1')
else:
    print(min(d))