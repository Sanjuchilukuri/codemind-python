n=int(input())
sum0=0
m=int(input())
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum0+=i
for i in range(1,m):
    if(m%i==0):
        sum1+=i
if(sum1==n and sum0==m):
    print("Amicable")
else:
    print("Not Amicable")