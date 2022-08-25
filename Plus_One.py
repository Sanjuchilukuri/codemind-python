n=int(input())
l=list(map(int,input().split()))
k=0
j=n-1
m=[]
for i in l:
    k=k+(i*(10**j))
    j=j-1;
k=k+1;
while(k!=0):
    p=k%10
    m.append(p)
    k=k//10
m.reverse()
print(*m)