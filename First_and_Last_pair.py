n=int(input())
l=list(map(int,input().split()))
q=[]
if n%2!=0:
    i=0
    j=len(l)-1
    while(i<=j):
        if i==j:
            q.append(l[i])
            q.append(0)
            i+=1
        else:
            q.append(l[i])
            q.append(l[j])
            i+=1
            j-=1
    print(*q)
else:
    i=0
    j=len(l)-1
    while(i<j):
        q.append(l[i])
        q.append(l[j])
        i+=1
        j-=1
    print(*q)
