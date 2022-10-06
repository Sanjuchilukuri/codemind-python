n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
q=list(set(l))
c=0
for i in q:
    if i in l1:
        c+=1
print(c)