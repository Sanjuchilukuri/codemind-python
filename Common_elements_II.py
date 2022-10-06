n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
q=[]
c=0
for i in l:
    if i not in l1:
        q.append(i)
for i in l1:
    if i not in l:
        q.append(i)
print(*q)