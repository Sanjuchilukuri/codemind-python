t=int(input())
c=0
while(t):
    x=input()
    if(x=="X++" or x=="++X"):
       c+=1
    else:
        c-=1
    t-=1
print(c)