n=input()
flag=0
if(n[0]=='-'):
    i=int(n)
    i=i*(-1)
    n=str(i)
    flag=1
    
if(n[len(n)-1]=="0"):
    i=int(n)
    s=i//10
    n=str(s)
if(flag==0):
    print(n[::-1])
else:
    print("-"+n[::-1])