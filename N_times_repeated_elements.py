n=int(input())
l=list(map(int,input().split()))
z=int(input())
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
q=[]
for k,v in d.items():
    if v==z:
        q.append(k)
if(len(q)>0):
    print(*q)
else:
    print(-1)