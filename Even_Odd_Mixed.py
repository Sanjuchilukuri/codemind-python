def doo(n,l):
    while(n):
        r=n%10
        l.append(r)
        n//=10
    l.reverse()
    


n=int(input())
l=[]
doo(n,l)
c=0
z=0
for i in l:
    if i%2==0:
        c+=1
    else:
        z+=1
if(c==len(l)):
    print("Even")
elif(z==len(l)):
    print("Odd")
else:
    print("Mixed")