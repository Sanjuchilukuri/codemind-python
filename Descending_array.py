n=int(input())
l=list(map(int,input().split()))
c=0
#print(l)
for i in range(0,len(l)-1):
    #print(l[i],"-",l[i+1])
    if l[i]>l[i+1]:
        c+=1
if(c==n-1):
    print("yes")
else:
    print("no")