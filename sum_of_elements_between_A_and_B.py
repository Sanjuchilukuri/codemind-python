n=int(input())
arr=list(map(int,input().split()))
l=[]
#k=[]
Sum=0
a,b=map(int,input().split())
for i in range(a,b+1):
    l.append(i)
for i in arr:
    if  i  in l:
        #k.append(i)
        Sum=Sum+i
print(Sum)