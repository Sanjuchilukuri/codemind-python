def fib(n):
    a,b=0,1
    print(a,b,end=' ')
    i=2
    while i<n:
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        i+=1
n=int(input())
fib(n)