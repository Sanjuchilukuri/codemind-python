n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
s=[]
c=0
for i in l:
    if i in l1 and i not in s:
        s.append(i)
print(*s)