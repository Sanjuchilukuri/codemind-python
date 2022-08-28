t=int(input())
while(t):
    n,a,b,k=map(int,input().split())
    c=n//a
    z=n//b
    if(c+z>=k):
        print("Win")
    else:
        print("Lose")
    t-=1
            