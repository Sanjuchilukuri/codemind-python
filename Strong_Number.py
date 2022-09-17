
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
n=int(input())
temp=n
add=0
while(n>0):
    r=n%10
    add+=fact(r)
    n//=10
if(add==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")