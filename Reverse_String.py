l=list(map(str,input().split()))
l1=l
s1=""
l1.reverse()
for i in range(len(l1)):
    if i==0:
        s1+=l1[i]
    else:
        s1+=" "+l1[i]
print(s1)