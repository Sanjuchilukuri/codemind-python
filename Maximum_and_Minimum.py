n=int(input())
l=list(map(int,input().split()))
d={}
flag=1
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
q=[]
for k,v in d.items():
    if(k==v):
        q.append(v)
        flag=0
if(flag==1):
    print(-1)
else:
    #print(l)
    print(min(q),max(q))