def fib(n):
    if(n==0):
        print(0)
        return
    a=0
    b=1
    c=a+b
    while(c<=n):
        a=b
        b=c
        c=a+b
    dif=abs(c-n)
    dif1=abs(b-n)
    if(dif>dif1):
        print(b)
    elif(dif1>dif):
        print(c)
    else:
        print(b,c)
    
    return









n=int(input())
fib(n)