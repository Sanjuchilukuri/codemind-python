n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
a=set(l)
b=set(l1)
c=list(a)
co=0
d=list(b)
for i in c:
    if i not in d:
        co+=1
for i in d:
    if i not in c:
        co+=1
print(co)