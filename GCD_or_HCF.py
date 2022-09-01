def gcd(n,m):
    if(m==0):
        return n
    if(n<m):
        return gcd(n,m%n)
    else:
        temp=n
        n=m
        m=temp
        return gcd(n,m)
n,m=map(int,input().split())
print(gcd(n,m))