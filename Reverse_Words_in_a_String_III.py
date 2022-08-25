l=list(map(str,input().split()))
l1=[]
for i in l:
    s1=i[::-1]
    l1.append(s1)
n1=len(l1)
s1=""
for i in range(n1):
    if i==0:
        s1=s1+l1[i]
    else:
        s1=s1+" "+l1[i]
    
print(s1)