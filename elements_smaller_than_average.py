n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
c=0
for i in l:
    if i<=avg:
        c+=1
print(c)