def gcd(a,b):
    if(b==0 ):
        return a
    if(a==0):
        return b
    if(a>b):
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
    
a,b=map(int,input().split())
ans=(a*b)//gcd(a,b)
print(ans)
