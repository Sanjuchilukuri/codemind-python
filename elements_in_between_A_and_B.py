n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
N=[]
for i in l:
    if i>=a and i<=b:
        N.append(i)
if len(N)==0:
    print(-1)
else:
    print(*N)