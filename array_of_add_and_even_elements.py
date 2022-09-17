n=int(input())
l=list(map(int,input().split()))
o=[]
for i in l:
    if i%2!=0:
        o.append(i)
for i in l:
    if i%2==0:
        o.append(i)
print(*o)